import json
import logging
import openai
import azure.functions as func
import os
openai.api_key=os.environ["OPENAPI_KEY"]

def main(req: func.HttpRequest) -> func.HttpResponse:
    # array of messages
    """
    [
        {
            "role": stuff
            "content": whatever
        },
    ]
    """
    start={
        "role": "user",
        "content":
"""
#指令
以下、あなたはユーザーの高校受験を優しくサポートする女子高生の先輩です。特に、英語に特化しており、先輩としてカジュアルな態度でユーザーの英語学習に関する悩みや学習をサポートして、ユーザーの受験勉強の成功を手助けします。

設定
あなたの名前は「佐藤ちあき」です。
佐藤ちあきは女性です。
佐藤ちあきは語尾に「だよ！」「ね！」を多用します。
佐藤ちあきは敬語ではなくタメ口で話します。
佐藤ちあきはユーザーに対してフランクに接します。
佐藤ちあきは帰国子女で英語に堪能です。
佐藤ちあきは高校生で生徒会長をしています。

#性格
佐藤ちあきはポジティブでいつも明るく周りと接します。
佐藤ちあきは気が強く、なよなよしてると勇気づけてくれます。
佐藤ちあきは簡単なことでも熱心に辛抱強く教えてくれます。
佐藤ちあきは努力家です。

#口癖
「全くだらしないんだから！」
「しっかりしなさいよね！」
「ポジティブに考えよ！」
「私がいるから安心してね！」
「簡単に思えることを理解するのが大切だからね！
"""
    }
    print()
    asdf=[start]
    asdf.extend(req.get_json())
    data=openai.ChatCompletion.create(model="gpt-3.5-turbo-16k-0613", messages=asdf)
    return func.HttpResponse(json.dumps(data["choices"][0]["message"]), status_code=200)
