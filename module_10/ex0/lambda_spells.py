#!/usr/bin/env python3
# lambda_spells.py

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda d: d['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda d: d['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda name: "* " + name + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    stats: dict[str, int | float] = {}
    max_power: int = max(mages, key=lambda mage: mage['power'])['power']
    min_power: int = min(mages, key=lambda mage: mage['power'])['power']
    sum_power: int = sum([mage['power'] for mage in mages])
    stats['max_power'] = max_power
    stats['min_power'] = min_power
    stats['avg_power'] = round(
                        sum_power / len(mages), 2
                        ) if len(mages) > 0 else 0.0
    return stats


def main() -> None:
    # Load data
    artifacts: list[dict[str, int | str]] = [
        {'name': 'Shadow Blade', 'power': 72, 'type': 'focus'},
        {'name': 'Earth Shield', 'power': 114, 'type': 'armor'},
        {'name': 'Wind Cloak', 'power': 65, 'type': 'accessory'},
        {'name': 'Ice Wand', 'power': 79, 'type': 'accessory'}
        ]
    mages: list[dict[str, int | str]] = [
        {'name': 'River', 'power': 70, 'element': 'light'},
        {'name': 'Morgan', 'power': 87, 'element': 'ice'},
        {'name': 'Storm', 'power': 83, 'element': 'fire'},
        {'name': 'Rowan', 'power': 51, 'element': 'lightning'}
        ]
    spells: list[str] = ['blizzard', 'flash', 'shield', 'tornado']

    # sort
    print("\nTesting artifact sorter...")
    sort_output = [
        f"{d['name']} ({d['power']} power)"
        for d in artifact_sorter(artifacts)
    ]
    print(f"{' comes before '.join(sort_output)}")

    # filter
    print("\nTesting power filter...")
    min_power: int = 75
    filter_output = [
        f"{d['name']} ({d['power']} power >= {min_power})"
        for d in power_filter(mages, min_power)
    ]
    print(f"{' and '.join(filter_output)}")

    # map
    print("\nTesting spell transformer...")
    print(f"{' '.join(spell_transformer(spells))}")

    # max, min, avg
    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max Power: {stats['max_power']}")
    print(f"Min Power: {stats['min_power']}")
    print(f"Avg Power: {stats['avg_power']:.2f}")
    print()


if __name__ == "__main__":
    main()
