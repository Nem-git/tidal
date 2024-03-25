from pick import pick
liste = ["A", "B", "C"]

choices = pick(
    liste,
    title=(
        f"search.\n"
        "Press SPACE to select, RETURN to download, CTRL-C to exit."
    ),
    multiselect=True,
    min_selection_count=1,
)

#DOESNT WORK WTF I HATE THIS