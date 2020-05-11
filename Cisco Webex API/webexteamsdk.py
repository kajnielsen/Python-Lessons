from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI (
    access_token = "Y2ZjYzI5YWMtYWE3NC00ZGJjLWIzOTAtNDE2NjVhYjFlMzY2M2YyMzdmOWEtMTE4_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

)

#print(api.people.me())
rooms = api.rooms.list()
for r in rooms:
    api.messages.create(roomId = r.id, text = "From Denmark with Love!")

