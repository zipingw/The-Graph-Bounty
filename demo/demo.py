import requests
import argparse

def query_the_graph():
    # The Graph的API端点
    url = "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2"
    url2 = "https://gateway-arbitrum.network.thegraph.com/api/[api-key]/subgraphs/id/3Tk2gHEvpbFELWw5VN9fxFWV6c8oaZC6qhoVNWVgZiun"
    url3 = "https://api.studio.thegraph.com/query/81405/censored/v0.0.1"

    # GraphQL查询
    query = """
    {
    adminApproveds(first: 5) {
        id
        account
        sender
        blockNumber
    }
    adminRevokeds(first: 5) {
        id
        account
        sender
        blockNumber
    }
    }
    """

    # 发送请求
    response = requests.post(url3, json={'query': query})

    # 解析响应
    data = response.json()

    # 打印结果
    if 'data' in data:
        print(data)
    else:
        print("Error in query response:", data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query The Graph API and print results.")
    args = parser.parse_args()
    query_the_graph()
