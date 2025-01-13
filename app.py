import streamlit as st
import pandas as pd

def main():
    st.title("📅 Student's Daily Timetable Generator")
    st.write("Plan your day effectively by creating a timetable.")

    # Input fields for timetable details
    st.header("Add Subjects and Time Slots")
    num_subjects = st.number_input("How many subjects do you want to plan for?", min_value=1, max_value=10, value=5, step=1)

    subjects = []
    for i in range(num_subjects):
        subject = st.text_input(f"Subject {i + 1} Name", value=f"Subject {i + 1}")
        start_time = st.time_input(f"Start Time for {subject}", key=f"start_time_{i}")
        end_time = st.time_input(f"End Time for {subject}", key=f"end_time_{i}")
        subjects.append({"Subject": subject, "Start Time": start_time, "End Time": end_time})

    # Add breaks
    st.header("Add Breaks")
    add_breaks = st.checkbox("Add breaks between subjects?")
    if add_breaks:
        break_time = st.number_input("Break duration (in minutes):", min_value=1, max_value=60, value=15, step=1)
    else:
        break_time = 0

    # Generate timetable button
    if st.button("Generate Timetable"):
        timetable = []
        for subject in subjects:
            timetable.append({
                "Activity": subject["Subject"],
                "Start Time": subject["Start Time"].strftime("%H:%M"),
                "End Time": subject["End Time"].strftime("%H:%M")
            })
            if add_breaks:
                break_start = pd.to_datetime(subject["End Time"]) + pd.Timedelta(minutes=break_time)
                break_end = break_start + pd.Timedelta(minutes=break_time)
                timetable.append({
                    "Activity": "Break",
                    "Start Time": break_start.time().strftime("%H:%M"),
                    "End Time": break_end.time().strftime("%H:%M")
                })

        # Convert timetable to DataFrame for display
        df = pd.DataFrame(timetable)
        st.subheader("Your Timetable:")
        st.table(df)

if __name__ == "__main__":
    main()
