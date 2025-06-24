import time
from pypet import Environment

# 🐶 Define your adorable pet with mood logic and state flags
class Pet:
    def __init__(self, name):
        self.name = name
        self.state = {
            'hungry': True,
            'sleepy': False,
            'playful': True,
            'energy': 100,
        }

    def update_state(self):
        self.state['energy'] -= 10
        self.state['hungry'] = self.state['energy'] < 50
        self.state['sleepy'] = self.state['energy'] < 30
        self.state['playful'] = self.state['energy'] > 40

    def mood_message(self):
        if self.state['sleepy']:
            return "😴 Zzz... I'm super sleepy!"
        elif self.state['hungry']:
            return "🍽️ Feed me please! My tummy's rumbling!"
        elif self.state['playful']:
            return "🐾 Let’s play! I’m full of energy!"
        else:
            return "😌 I'm chilling and feeling alright."

    def __str__(self):
        return f"{self.name} says: {self.mood_message()}"

# 🧪 Real-time simulation using Pypet
def simulate_pet(traj):
    pet = Pet('Fruities🍇🥑')
    for t in range(traj.run_duration):
        pet.update_state()
        print(pet)
        time.sleep(1)

# 🚀 Set up the Pypet environment
env = Environment(
    trajectory='pet_sim',
    filename='pet_data.hdf5',
    overwrite_file=True
)

traj = env.trajectory
traj.f_add_parameter('run_duration', 10)

# 🏁 Run the simulation
env.run(simulate_pet)