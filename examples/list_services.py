from banyan.api import BanyanApiClient
c = BanyanApiClient(api_server_url='https://dev02.console.bnntest.com',refresh_token="eyJhbGciOiJSUzI1NiIsImtpZCI6ImZjNTg5Mjg3YzQxNDkzYjI1MDAyYzM2YzQxZDZiMGI0YWFjZTgxMWMiLCJ0eXAiOiJKV1QifQ.eyJBY2Nlc3NUb2tlbiI6ImxldmVsMSIsIkF1dGgiOiJMT0NBTCIsIkVtYWlsIjoiIiwiTm9WUE4iOiJESVNBQkxFRCIsIk9yZ0lEIjoiIiwiUHJvZmlsZSI6IlJlYWRPbmx5IiwiUmVmcmVzaCI6InRydWUiLCJSZWZyZXNoRW1haWwiOiJhbmtpdC5rdW1hckBqb3Noc29mdHdhcmUuY29tIiwiVVVJRCI6IiIsIlVuaXF1ZUlEIjoiNmJkYzBjMmMtNjhjMi00MmZmLWFkMjgtNjFjMDMxZTExMWJjIiwiZXhwIjoxNjY2MTcyNjY5LCJpYXQiOjE2NjYxNzI2Njh9.i29gQ2M2jTMhqP1pNupb0MAErjJQL0GV7obwnOtiU3ZZoJ42XTnHky7J5VGpZ79AVtiqTcUE-Eie_KBQ02l_2VKquiYSG51jqyhcSHZs2FQblgm3NXNHj_1JWX_bVYTlgZi7gQFJal97IOC3mEJTg8S3VVVi8LuY1G34jKpVpqiHVPhnQXJYHzOr-HkOT-laFU5X97aTKq24zQUoxsE_-05jsJaqu2Q-tSdqtoSt8b_c3H1NPM6ydxeKWEzIHRi1hyBAAac0xHPJSn_xGbmh_pNqCuhmHzeDk5MQT7M_zW9x7rUzgTwGP8iSMGg_eFRVMIVn-0Qjkjb_JdaRjotBVg")
# for service in c.services.list():
#     print(service.name)
#     service.disable()
#     if service.name == 'test-service':
#         service.disable("test-service")
# c.services.disable("test-service.ankitdev02-shield.bnn")
c.services.enable("test-service.ankitdev02-shield.bnn")

