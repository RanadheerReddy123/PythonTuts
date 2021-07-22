class VivoMobile:
    def __init__(self):
        self.model = 'model'
        self.ram = 'ram'
        self.rom = 'rom'

    def info(self):
        print('Vivo', self.model, 'Info:')
        print('Model', self.model)
        print('RAM', self.ram)
        print('ROM', self.rom)
        print('')

mobile1 = VivoMobile()
mobile1.model = 'V20'
mobile1.ram = '8GB'
mobile1.rom = '64GB'
mobile1.info()

mobile2 = VivoMobile()
mobile2.model = 'X50'
mobile2.ram = '16GB'
mobile2.rom = '128GB'
mobile2.info()

mobile3 = VivoMobile()
mobile3.model = 'Y51'
mobile3.ram = '8GB'
mobile3.rom = '32GB'
mobile3.info()