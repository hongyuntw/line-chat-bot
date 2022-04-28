# Line Bot
from flask import Flask, request, abort, render_template
from urllib.request import urlopen
from config import line_channel_access_token, line_channel_secret
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
import os
from flex_msg import experience_flex, award_flex, resume_flex
################################

from linebot.models import *


app = Flask(__name__)



# Channel Access Token
line_bot_api = LineBotApi(line_channel_access_token)
# Channel Secret
handler = WebhookHandler(line_channel_secret)


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'




@handler.add(FollowEvent)
def handle_follow_event(event):
    line_bot_api.reply_message(  # 回復傳入的訊息文字
        event.reply_token,
        TemplateSendMessage(
            alt_text='指令提示',
            template=ButtonsTemplate(
                # title='現在有的功能',
                text='歡迎點擊查看~~',
                actions=[
                    MessageTemplateAction(
                        label='個人簡介',
                        text='cv'
                    ),
                    MessageTemplateAction(
                        label='實習經驗',
                        text='實習'
                    ),
                    MessageTemplateAction(
                        label='比賽經驗',
                        text='比賽'
                    )
                ]
            )
        )
    )



# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    text = text.lower().strip()
    # profile = line_bot_api.get_profile(event.source.user_id)

    if text == "cv":
        contents = resume_flex()
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage('歡迎查看姜宏昀的個人簡介', contents)
        )

    elif text == "實習":
        contents = experience_flex()
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage('歡迎查看我的實習經歷', contents)
        )

    elif text == '競賽' or text == '比賽':
        contents = award_flex()
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage('歡迎查看我的競賽經驗', contents)
        )
    elif text == '指令' or text == '提示':
        line_bot_api.reply_message(  # 回復傳入的訊息文字
        event.reply_token,
        TemplateSendMessage(
            alt_text='指令提示',
            template=ButtonsTemplate(
                # title='現在有的功能',
                text='歡迎點擊查看~~',
                actions=[
                    MessageTemplateAction(
                        label='個人簡介',
                        text='cv'
                    ),
                    MessageTemplateAction(
                        label='實習經驗',
                        text='實習'
                    ),
                    MessageTemplateAction(
                        label='比賽經驗',
                        text='比賽'
                    )
                ]
            )
        )
    )


    

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

    