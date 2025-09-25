import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import os
    from pathlib import Path

    import marimo as mo
    import polars as pl
    import polars.selectors as cs
    return Path, cs, mo, os, pl


@app.cell
def _():
    COMPLETION_COLUMNS = {
        "YMHA Cohort 3 Student Applet IN PERSON": [
            "AMHLQ",
            "Healthcare Access",
            "Impact and Professional Importance",
            "MAP + MH Interest",
            "MEIM-6",
            "Mental Health Attitudes and Help-Seeking",
            "Mental Healthcare",
            "PCRB",
            "PEARLS + CRISIS",
            "PSC",
            "SCCS",
            "SCCT",
            "SEHS-HE",
            "Student Week 1 Assessment",
            "Student Week 2 Assessment",
            "Student Week 3 Assessment",
        ],
        "YMHA Cohort 3 Student Applet VIRTUAL": [
            "Adolescent Mental Health Literacy Questionnaire (AMHLQ)",
            "Healthcare Access",
            "Impact and Professional Importance",
            "MAP + Mental Health Interest",
            "Multigroup Ethnic Identity Measure–Revised (MEIM-6)",
            "Mental Health Attitudes and Help-Seeking",
            "Mental Healthcare",
            "Perceived Campus Resources and Barriers (PCRB)",
            "PEARLS + CRISIS",
            "Pediatric Symptom Checklist (PSC)",
            "Student Connectedness to Community Scale (SCCS)",
            "Social Cognitive Career Theory (SCCT)",
            "Social Emotional Health Survey – Higher Education (SEHS-HE)",
            "Student Week 1 Assessment",
            "Student Week 2 Assessment",
            "Student Week 3 Assessment",
        ],
        "YMHA Cohort 3 Teacher Applet IN PERSON": ["Week 1", "Week 2", "Week 3"],
        "YMHA Cohort 3 Teacher Applet VIRTUAL": ["Week 1", "Week 2", "Week 3"],
        "YMHA Cohort 3 Mentor Applet": [
            "Brief Version of the Big Five Personality Inventory (BFI)",
            "Check-In",
            "Experience",
            "Multigroup Ethnic Identity Measure–Revised (MEIM-6)",
            "Mentor Experience",
            "MinT Mentoring Styles Questionnaire",
            "Program-Developed",
            "The MAP",
        ],
        "YMHA Cohort 3 Parent Applet": [
            "Confidence",
            "DSM-5 Cross-Cutting Symptom Measure",
            "Demographic",
            "Inventory of Family Protective Factors (IFPF)",
            "Pediatric Symptom Checklist (PSC)",
            "Stigma and Self-Stigma Scales (SASS)",
        ],
    }
    return (COMPLETION_COLUMNS,)


@app.cell(hide_code=True)
def _(COMPLETION_COLUMNS, mo, os):
    participants_file = mo.ui.file()
    data_file = mo.ui.file()
    run_button = mo.ui.run_button()
    output_dir = mo.ui.text(label="Output Dir", value="output/")
    applet_name = mo.ui.dropdown(
        label="Applet Name", options=COMPLETION_COLUMNS.keys()
    )
    date_format = mo.ui.text(label="Date Format", value="%F %T%.f")
    mo.vstack(
        [
            mo.md(f"Current dir: {os.getcwd()}"),
            mo.hstack(
                [mo.md("#### Upload participants file"), participants_file],
                justify="start",
            ),
            mo.hstack(
                [mo.md("#### Upload data file"), data_file], justify="start"
            ),
            output_dir,
            applet_name,
            date_format,
            run_button,
        ]
    )
    return (
        applet_name,
        data_file,
        date_format,
        output_dir,
        participants_file,
        run_button,
    )


@app.cell
def _(cs, mo, participants_file, pl, run_button):
    def load_participants(data) -> pl.DataFrame:
        """Load participants from file path in extra args."""
        participants = pl.read_csv(data)
        if "site" not in participants.columns:
            raise Exception("'site' column not found in YMHA participants file")
        if "secretUserId" not in participants.columns:
            raise Exception(
                "'secretUserId' column not found in YMHA participants file"
            )
        return participants.select(
            pl.col("secretUserId").alias("secret_id"),
            pl.col("nickname"),
            pl.col("firstName").alias("first_name"),
            pl.col("lastName").alias("last_name"),
            "site",
            cs.matches("^room$"),
        )


    mo.stop(not run_button.value, mo.md(""))
    participants_data = load_participants(participants_file.contents())
    return (participants_data,)


@app.cell
def _(applet_name, data_file, date_format, mo, pl, run_button):
    def load_data(mindlogger_data) -> pl.DataFrame:
        """Load data."""
        ml_data = pl.read_csv(
            mindlogger_data,
            # try_parse_dates=True,
            # schema_overrides={"response_start_time": pl.Datetime()},
        )
        if applet_name.value:
            ml_data = ml_data.filter(pl.col("applet_name") == applet_name.value)
        return (
            ml_data.select(
                pl.col("activity_name").str.strip_chars(),
                pl.col("secret_user_id").alias("secret_id"),
                pl.col("response_start_time")
                .str.to_datetime(date_format.value)
                .dt.date()
                .alias("activity_date"),
            )
            .unique()
            .with_columns(activity_completed=pl.lit(True))
        )


    mo.stop(not run_button.value, mo.md(""))
    data = load_data(data_file.contents())
    return (data,)


@app.cell
def _(cs, pl):
    def calc_attendance(
        df: pl.DataFrame, participants: pl.DataFrame
    ) -> list[tuple[str, pl.DataFrame]]:
        attendance = df.pivot(
            on="activity_name",
            values="activity_completed",
            sort_columns=True,
            maintain_order=True,
            aggregate_function=pl.element().any(),
        )
        dates = attendance.select(pl.col("activity_date").unique()).filter(
            pl.col("activity_date").is_not_null()
        )
        participant_dates = participants.join(dates, how="cross")
        all_attendance = participant_dates.join(
            attendance,
            on=["secret_id", "activity_date"],
            how="left",
        ).with_columns(pl.col("^Student Check.*$").fill_null(False))  # noqa: FBT003
        part_dfs = all_attendance.partition_by(
            ["site", "activity_date"], as_dict=True
        )
        return [(("ymha_attendance-all",), all_attendance)] + [
            ((f"site_{part[0]}", f"date_{part[1]}", f"ymha_attendance"), df)
            for part, df in part_dfs.items()
        ]
        # returns list[tuple[tuple[str], dataframe]]
        # list of outputs. each output is a tuple of path and dataframe. path is a tuple of path segments.


    def calc_completion(
        df: pl.DataFrame,
        participants: pl.DataFrame,
        completion_columns: list[str],
    ) -> list[tuple[str, pl.DataFrame]]:
        completion = df.drop("activity_date").pivot(
            on="activity_name",
            values="activity_completed",
            aggregate_function=pl.element().any(),
            maintain_order=True,
            sort_columns=True,
        )
        identifier_col_selector = cs.by_name(
            "secret_id",
            "nickname",
            "first_name",
            "last_name",
            "site",
        ) | cs.matches(r"^room$")
        activity_col_selector = ~identifier_col_selector
        all_completion = participants.join(
            completion, on="secret_id", how="left"
        ).select(
            identifier_col_selector,
            activity_col_selector.fill_null(False),  # noqa: FBT003
        )
        print(all_completion.columns)
        all_completion = (
            all_completion.with_columns(
                complete=pl.concat_list(completion_columns).list.all(),
                partially_complete=pl.concat_list(completion_columns).list.any(),
            )
            .with_columns(
                complete=pl.when(pl.col("complete"))
                .then(pl.lit("TRUE"))
                .when(pl.col("partially_complete"))
                .then(pl.lit("PARTIALLY TRUE"))
                .otherwise(pl.lit("FALSE"))
            )
            .drop("partially_complete")
        )
        site_completion = all_completion.partition_by("site", as_dict=True)
        return (
            [
                (("ymha_completion-all",), all_completion),
                (
                    ("ymha_completion_summary-all",),
                    all_completion.select(identifier_col_selector, "complete"),
                ),
            ]
            + [
                ((f"site_{part[0]}", "ymha_completion"), df)
                for part, df in site_completion.items()
            ]
            + [
                (
                    (
                        f"site_{part[0]}",
                        f"ymha_completion_summary",
                    ),
                    df.select(identifier_col_selector, "complete"),
                )
                for part, df in site_completion.items()
            ]
        )
    return calc_attendance, calc_completion


@app.cell
def _(
    COMPLETION_COLUMNS,
    applet_name,
    calc_attendance,
    calc_completion,
    data,
    mo,
    participants_data,
    pl,
    run_button,
):
    mo.stop(not run_button.value, mo.md(""))
    _partitioned_activities = data.with_columns(
        is_ema=pl.col("activity_name").str.starts_with("Student Check")
    ).partition_by("is_ema", as_dict=True, include_key=False)

    outputs = (
        calc_attendance(_partitioned_activities[(True,)], participants_data)
        if (True,) in _partitioned_activities
        else []
    ) + (
        calc_completion(
            _partitioned_activities[(False,)],
            participants_data,
            COMPLETION_COLUMNS[applet_name.value],
        )
        if (False,) in _partitioned_activities
        else []
    )
    outputs
    return (outputs,)


@app.cell
def _(Path, cs, mo, output_dir, outputs, run_button):
    mo.stop(not run_button.value, mo.md(""))

    _output_dir = Path(output_dir.value)
    if not _output_dir.is_dir():
        _output_dir.mkdir(parents=True, exist_ok=True)
        print(f"Created output directory: {_output_dir}")

    for _path_segments, _df in outputs:
        _output_path = (
            _output_dir.joinpath(*_path_segments).with_suffix(".xlsx").resolve()
        )
        _output_path.parent.mkdir(parents=True, exist_ok=True)
        _df.write_excel(
            _output_path,
            conditional_formats={
                cs.all(): [
                    {
                        "type": "cell",
                        "criteria": "==",
                        "value": False,
                        "format": {"bg_color": "#FFC7CE"},
                    },
                    {
                        "type": "cell",
                        "criteria": "==",
                        "value": True,
                        "format": {"bg_color": "#97bfa2"},
                    },
                    {
                        "type": "text",
                        "criteria": "begins with",
                        "value": "FALS",
                        "format": {"bg_color": "#FFC7C1"},
                    },
                    {
                        "type": "text",
                        "criteria": "begins with",
                        "value": "TRU",
                        "format": {"bg_color": "#97bfa1"},
                    },
                    {
                        "type": "text",
                        "criteria": "begins with",
                        "value": "PARTIALLY TRUE",
                        "format": {"bg_color": "#e6e887"},
                    },
                ],
            },
        )

    print(f"{len(outputs)} outputs written.")
    disp = mo.md(f"{len(outputs)} outputs written.")
    disp
    return


if __name__ == "__main__":
    app.run()
