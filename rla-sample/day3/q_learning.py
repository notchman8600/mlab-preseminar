from collections import defaultdict
import gym
from el_agent import ELAgent
from frozen_lake_util import show_q_value


class QLearningAgent(ELAgent):

    def __init__(self, epsilon=0.1):
        super().__init__(epsilon)

    def learn(self, env, episode_count=1000, gamma=0.9,
              learning_rate=0.1, render=False, report_interval=50):
        self.init_log()
        actions = list(range(env.action_space.n))
        self.Q = defaultdict(lambda: [0] * len(actions))
        for e in range(episode_count):
            s = env.reset()
            done = False
            while not done:
                if render:
                    env.render()
                a = self.policy(s, actions)
                n_state, reward, done, info = env.step(a)
                # 報酬＋割引率*遷移先の価値 => r + γV(s)に対応
                # 価値が最大になるような行動を前提に算出 => valueベース
                # Q学習のQはQ(s,a)、つまり状態における行動の価値である
                # max(self.Q[n_state])はn_stateにおける状態の価値の最大値を取得する
                # これを足し合わせることでgainが最大化出来る
                gain = reward + gamma * max(self.Q[n_state])
                estimated = self.Q[s][a]
                self.Q[s][a] += learning_rate * (gain - estimated)
                s = n_state

            else:
                self.log(reward)

            if e != 0 and e % report_interval == 0:
                self.show_reward_log(episode=e)


def train():
    agent = QLearningAgent()
    env = gym.make(
        'FrozenLake-v1',
        desc=None,
        map_name="4x4",
        is_slippery=False)
    agent.learn(env, episode_count=500)
    show_q_value(agent.Q)
    agent.show_reward_log()


if __name__ == "__main__":
    train()
