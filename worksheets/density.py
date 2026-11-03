"""Calculate packed shipment density; no NMFC classification or rating."""
import csv
import json
import sys
from decimal import Decimal, InvalidOperation, localcontext

def calculate(path):
    with localcontext() as ctx:
        ctx.prec = 40
        records = []
        with open(path, newline='', encoding='utf-8-sig') as stream:
            reader = csv.DictReader(stream)
            required = ('length_in', 'width_in', 'height_in', 'weight_lb')
            if not set(required).issubset(reader.fieldnames or []):
                raise ValueError('Required columns: ' + ', '.join(required))
            for line, row in enumerate(reader, 2):
                values = [Decimal(row[key]) for key in required]
                if any(not value.is_finite() or value <= 0 for value in values):
                    raise ValueError(f'Line {line}: measurements must be positive and finite')
                length, width, height, weight = values
                volume = length * width * height / Decimal(1728)
                records.append({'record_id': row.get('record_id', str(line)),
                                **{key: str(value) for key, value in zip(required, values)},
                                'volume_ft3': str(volume)})
        if not records:
            raise ValueError('At least one handling unit is required')
        total_weight = sum(Decimal(row['weight_lb']) for row in records)
        total_volume = sum(Decimal(row['volume_ft3']) for row in records)
        return {'records': records, 'total_weight_lb': str(total_weight),
                'total_volume_ft3': str(total_volume),
                'density_lb_per_ft3': str(total_weight / total_volume),
                'formula': 'sum(weight_lb) / sum(length_in * width_in * height_in / 1728)',
                'limitation': 'Density only; not NMFC classification, freight class or a rate quote.'}

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: python density.py measurements.csv')
    try:
        print(json.dumps(calculate(sys.argv[1]), indent=2))
    except (ValueError, InvalidOperation, OSError) as error:
        sys.exit(str(error))
