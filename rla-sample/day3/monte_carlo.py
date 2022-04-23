import math
from collections import defaultdict
import gym
from el_agent import ELAgent
from frozen_lake_util import show_q_value


class MonteCarloAgent(ELAgent):

    def __init__(self, epsilon=0.1):
        super().__init__(epsilon)

    def learn(self, env, episode_count=1000, gamma=0.9,
              render=False, report_interval=50):
        self.init_log()
        # 行動リスト
        actions = list(range(env.action_space.n))
        # 行動価値が記録される
        self.Q = defaultdict(lambda: [0] * len(actions))
        # N[s][a]には状態sでaを撮った回数がカウントされる
        N = defaultdict(lambda: [0] * len(actions))
        # エピソード終了までプレイする
        for e in range(episode_count):
            s = env.reset()
            done = False
            # Play until the end of episode.
            experience = []
            while not done:
                if render:
                    env.render()
                a = self.policy(s, actions)
                n_state, reward, done, info = env.step(a)
                experience.append({"state": s, "action": a, "reward": reward})
                s = n_state
            else:
                self.log(reward)

            # Evaluate each state, action.
            # 各エピソードで取れるアクションの行動評価を行なう
            for i, x in enumerate(experience):
                s, a = x["state"], x["action"]

                # Calculate discounted future reward of s.
                G, t = 0, 0
                for j in range(i, len(experience)):
                    # 各状態における価値を取得する
                    G += math.pow(gamma, t) * experience[j]["reward"]
                    t += 1
                # 選択行動++
                N[s][a] += 1  # count of s, a pair
                # 学習率の計算
                alpha = 1 / N[s][a]
                # 割引現在価値を更新する
                self.Q[s][a] += alpha * (G - self.Q[s][a])

            if e != 0 and e % report_interval == 0:
                self.show_reward_log(episode=e)


def train():
    agent = MonteCarloAgent(epsilon=0.1)
    env = gym.make(
        'FrozenLake-v1',
        desc=None,
        map_name="4x4",
        is_slippery=True)
    agent.learn(env, episode_count=500)
    show_q_value(agent.Q)
    agent.show_reward_log()


if __name__ == "__main__":
    train()
