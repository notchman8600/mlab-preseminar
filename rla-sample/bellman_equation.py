# Valueベースのベルマン方程式のサンプルプログラム


def V(s, gamma=0.99):
    # 報酬の計算
    # 割引率を考慮する（γ=0.99）
    V = R(s) + gamma * max_V_on_next_state(s)
    return V


def R(s):
    # エピソード終了時の評価値
    if s == "happy_end":
        return 1
    elif s == "bad_end":
        return -1
    else:
        return 0


def max_V_on_next_state(s):
    # If game end, expected value is 0.
    # happy_endとbad_endが含まれていたら計算終了
    if s in ["happy_end", "bad_end"]:
        return 0
    # アクションを定義
    actions = ["up", "down"]
    values = []
    # up と downでループ
    for a in actions:
        # 遷移確率を計算
        transition_probs = transit_func(s, a)
        v = 0
        for next_state in transition_probs:
            prob = transition_probs[next_state]
            # 遷移確率 * 遷移先の価値
            # = prob * ( R(s)  + gamma * max_V_on_next_state(s))
            # 再帰的に終了条件（happy_end or bad_end）になるまで報酬を繰り返し計算する
            v += prob * V(next_state)
        values.append(v)
    # 全ての行動でvを計算し値が最大になる価値を選択する
    return max(values)


# ゲームを定義
def transit_func(s, a):
    """
    Make next state by adding action str to state.
    ex: (s = 'state', a = 'up') => 'state_up'
        (s = 'state_up', a = 'down') => 'state_up_down'
    """
    # 最初はstateなどの初期値が入る
    # アンダーバーが入るとそこで分割し、"state"を排除する
    actions = s.split("_")[1:]
    # ゲーム回数を定義
    LIMIT_GAME_COUNT = 5
    # 4回以上upしたら終了
    HAPPY_END_BORDER = 4
    # 選択した行動が反映される確率
    MOVE_PROB = 0.9

    def next_state(state, action):
        return "_".join([state, action])
    # ゲーム回数終了であればスコアを計算
    if len(actions) == LIMIT_GAME_COUNT:
        # upの回数を計測
        up_count = sum([1 if a == "up" else 0 for a in actions])
        # happy or badを決定
        state = "happy_end" if up_count >= HAPPY_END_BORDER else "bad_end"
        # 終了時の遷移確率は1
        prob = 1.0
        return {state: prob}
    else:
        # 選択行動の反対方向を算出
        opposite = "up" if a == "down" else "down"
        return {
            # 0.9で確率で選択通りの行動を取る
            next_state(s, a): MOVE_PROB,
            # 0.1の確率で捻くれる
            next_state(s, opposite): 1 - MOVE_PROB
        }


if __name__ == "__main__":
    print(V("state"))
    print(V("state_up_up"))
    print(V("state_down_down"))
