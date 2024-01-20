from pg_to_switch import main

# main(settings_file="settings_TD_east.yml", results_folder="test4")
main(
    settings_file="transmission_study/transmission_study_26z.yml",
    results_folder="test4",
    case_id=["full_2023"],
    year=[2023],
)
