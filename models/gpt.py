import openai

# アロナ(GPT3.5)の設定
arona_setting = ""
with open('character_setting/arona_setting.txt', 'r') as f:
    arona_setting = f.read()

class Gpt():
    def __init__(self, api_key) -> None:
        # APIキーの設定
        openai.api_key = api_key
        self.response = ''
        self.character_settings = arona_setting
        self.logs = []


    def print_logs(self):
        print('--- 現在までの会話ログ')
        if not len(self.logs):
            print('None')
            return
        
        for log in self.logs[1:]:
            role = log.get('role')
            context = log.get('content')
            print(f'role: {role}\t, content: {context}')

    def completion(self, msg: str):
        # 会話ログのリセット
        if msg == 'reset':
            self.response = '今までの会話の記憶を消去しました！'
            self.logs.clear()

            # ログを整形後表示
            self.print_logs()
            return self.response
        
        # 事前設定の適用
        if len(self.logs) == 0 and len(self.character_settings) != 0:
            sys_ctx = {"role": "system", "content": self.character_settings}
            self.logs.append(sys_ctx)


        # API用にtext整形, ログに追加
        new_message = {"role": "user", "content": msg}
        self.logs.append(new_message)

        # API呼び出し
        print('OpenAIのAPIを呼び出します。')
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.logs,
                timeout = 10
            )
            # ログに回答を追加
            res_ctx = {"role": "assistant", "content": response.choices[0].message.content}
            self.logs.append(res_ctx)

            # 回答と過去ログを整形後表示
            response_text = response.choices[0].message.content
            print(f'回答: {response_text}')
            # ログを整形後表示
            self.print_logs()
        except Exception as e:
            # タイムアウトのとき
            response_text = 'error: API呼び出しがタイムアウトしました。'
            print(f'タイムアウトしたっぽい\n{e}')
        
        return response_text
