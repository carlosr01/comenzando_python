import openai
from ics import Calendar
from datetime import datetime, timedelta
import argparse


def load_events(ics_path, days=7):
    """Load events for the next `days` days from an ICS file."""
    with open(ics_path, 'r', encoding='utf-8') as f:
        calendar = Calendar(f.read())

    now = datetime.now()
    upcoming = []
    for event in calendar.events:
        if event.begin.datetime >= now and event.begin.datetime <= now + timedelta(days=days):
            upcoming.append(event)
    return upcoming


def format_events(events):
    """Format events as text for summarization."""
    lines = []
    for e in events:
        begin = e.begin.humanize()
        end = e.end.humanize() if e.end else "no end"
        lines.append(f"- {e.name} ({begin} - {end})")
    return "\n".join(lines)


def summarize_events(events_text, model="gpt-3.5-turbo"):
    """Use OpenAI to summarize the list of events."""
    prompt = (
        "Resume brevemente las siguientes reuniones y recordatorios: \n\n" + events_text
    )
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()


def main():
    parser = argparse.ArgumentParser(description="Resume eventos de un calendario")
    parser.add_argument("ics_file", help="Archivo ICS de calendario")
    parser.add_argument("--days", type=int, default=7, help="Días a considerar")
    parser.add_argument("--model", default="gpt-3.5-turbo", help="Modelo de OpenAI")
    args = parser.parse_args()

    events = load_events(args.ics_file, args.days)
    if not events:
        print("No se encontraron eventos próximos")
        return
    text = format_events(events)
    summary = summarize_events(text, args.model)
    print("Resumen:\n")
    print(summary)


if __name__ == "__main__":
    main()
