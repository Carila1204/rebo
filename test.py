import pyupbit

access = "LOUpTVZJfvmLMqsxpjJJNC25fp8ugHGHNFfZWy97"          # 본인 값으로 변경
secret = "3KWbpgCM4s6WBk7CDokDeGyIifahxL2ypAkBxq8a"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
