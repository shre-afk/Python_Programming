# Task 5. Create a dictionary with the events in Dortmund and the date of the event. List all
# events that were running during the Night of Museums in Dortmund on 19th September 2026.



do_event = [
    {'event':"Boulder Night",'date':'21 Sept 2026'},
    {'event':"Hiking event",'date':'21 Oct 2026'},
    {'event':"Karaoke Night",'date':'19 Oct 2026'},
    {'event':"Essen light festival",'date':'19 Sept 2026'},
    {'event':"Kiosk Crawl",'date':'19 June 2026'},
    {'event':"Liar's Table",'date':'27 May 2026'},
    {'event':"Movie Night",'date':'6 Oct 2026'},
    {'event':"Westpark Tournament",'date':'01 Aug 2026'},
    {'event':"Werewolf Night",'date':'28 July 2026'},
    {'event':"Clay & Sip",'date':'19 Sept 2026'}
]

result = filter (lambda x: x['date'] == '19 Sept 2026',do_event)

print(list(result))