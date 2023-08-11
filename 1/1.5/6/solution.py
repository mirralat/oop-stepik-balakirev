class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name,  cpu, *mem):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mem[:self.total_mem_slots]

    def get_config(self):
        ret = [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                'Память: '+ ';'.join(map(lambda x: f'{x.name} - {x.volume}', self.mem_slots))]

        return ret

mb = MotherBoard('GigaByte', CPU('Intel', 2000), Memory('Kingston', 1000), Memory('Kingston', 2000))

