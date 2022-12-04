from utils import AOC

aoc = AOC(session='53616c7465645f5f4b51290a2179190526819ab8c1bd41d51b30dc44e3810b3adc1f27eac32a3835689e0c1d3b7cc60e')

#print(aoc.verify_session())

#aoc.get_today_file()

data = aoc.get_file(year=2020, day=7).analyse().head().data

