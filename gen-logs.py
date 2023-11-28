import argparse
import random

def gen_logs(ts, duration, output):
  hostnames = [f'hostname{x}' for x in range(1, 10)]
  users = [f'uid{x}' for x in range(1, 100)]

  with open(output, 'w') as f:
    while duration > 0:
      events = 10_000
      timestamps = sorted(random.sample(range(ts, ts + 59_999),  20_000))

      for t in timestamps:
        f.write(f'created={int(t/1000)}&hostname={random.choice(hostnames)}&uid={random.choice(users)}\n')

      duration -= 1
      ts += 60_000

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Generate logs')
  parser.add_argument('--ts', type=int, default=0, help='Start timestamp')
  parser.add_argument('--duration', type=int, default=60, help='Duration in minutes')
  parser.add_argument('--output', type=str, default="api.log", help='Output file')
  args = parser.parse_args()
  gen_logs(args.ts, args.duration, args.output)
