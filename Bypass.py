import httpx, random
from itertools import cycle
class variousAPI:
    GET_DATA = "https://discord.com/api/v9/guilds/{}/member-verification"
    SEND_DATA = "https://discord.com/api/v9/guilds/{}/requests/@me"
def Gettokens():
    with open('tokens.txt', 'r') as temp_file:
        token = [line.rstrip('\n') for line in temp_file]
    return token
token = Gettokens()
tokens_pool = cycle(token)
def requestsJoin(discordServerId, requestsData, accountToken):
    def RandomString(Length):
        Letter = "abcdefghijklmnopqrstuvwxyz0123456789"
        Message = ''
        for _ in range(0, Length):
            Message += Letter[random.randint(0, len(Letter) - 1)]
        return Message

    try:
        responseData = httpx.put(
            variousAPI.SEND_DATA.format(discordServerId),
            headers={"authorization":accountToken, "cache-control":"no-cache", "content-type":"application/json", "cookie":f"__cfuid={RandomString(43)}; __dcfduid={RandomString(32)}; locale=en-US", "origin":"https://discord.com", "pragma":"no-cache", "referer":"http://discord.com/channels/@me", "sec-ch-ua":'Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"', "sec-ch-ua-mobile":"?0", "sec-ch-ua-platform":"Windows", "sec-fetch-dest":"empty", "sec-fetch-mode":"cors", "sec-fetch-site":"same-origin", "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47", "x-debug-options":"bugReporterEnabled", "x-super-properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InRoIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk0LjAuNDYwNi44MSBTYWZhcmkvNTM3LjM2IEVkZy85NC4wLjk5Mi40NyIsImJyb3dzZXJfdmVyc2lvbiI6Ijk0LjAuNDYwNi44MSIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMDEwNzQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"},json=requestsData).json()
        try:
            if (responseData['message'] == "This feature has been temporarily disabled"):
                print(responseData['message'] + "on this server")
        except:
            try:
                responseData['guild_id']
                print('bypassed screening')
            except:
                pass
    except:
        print("already screened for token")
discordServerId = input("Server id: ")
while True:
    accountToken = next(tokens_pool)
    requestsData = httpx.get(variousAPI.GET_DATA.format(discordServerId), headers={"authorization": accountToken}).json()
    requestsJoin(discordServerId, requestsData, accountToken)