# Freight Shipping Worksheets

Reusable worksheets for measuring palletized freight and recording pallet disposition decisions.

The accompanying explanations are maintained at [Freight Class Desk](https://freightclassdesk.com/).

## Files

- `site-resource-inventory.csv`: a live HTTP-checked inventory of source resources, including source URLs, check timestamps, status codes and downloaded byte counts. These are measured web-resource metadata, not observed freight measurements.

- `density.py`: calculate total packed volume and shipment density from a CSV, using only the Python standard library.
- `measurements-example.csv`: explicitly hypothetical input; replace it with your actual packed measurements.
- `shipment-evidence-checklist.md`: a checklist for reconciling measurement, classification and billing evidence.
- `pallet-disposition.csv`: the site's existing blank disposition record.
- `pallet-disposition-fields.md`: field definitions and limitations.

## Run

```sh
python density.py measurements-example.csv
```

Each row represents one handling unit, with dimensions in inches and gross weight in pounds. Include the pallet and packaging in the measured unit. Repeated units require repeated rows. Volume = sum(length_in * width_in * height_in / 1728); density = sum(weight_lb) / total_volume_ft3. The conversion divisor follows from 12 inches per foot cubed. No rounding is applied before division.

The example uses invented measurements: 48 x 40 x 60 inches and 400 pounds; 48 x 40 x 48 inches and 600 pounds. They are demonstration inputs, not observed shipments. The script prints the calculation and each input.

The tool does not assign an NMFC item, confirm freight class, quote a rate, authorize pallet repair or certify load capacity. Applicable commodity classification, carrier pricing and repair specifications must be checked separately.

## Sources and provenance

- Measurement workflow: https://freightclassdesk.com/freight-density-calculator-pallet-weight/
- Density aggregation: https://freightclassdesk.com/multiple-pallet-density-average/
- Shipment evidence: https://freightclassdesk.com/nmfc-calculator/
- Blank disposition record and its context: https://freightclassdesk.com/when-to-repair-or-scrap-a-pallet/

The checklist and field guide are editorial workflow aids derived from the owner's website, not standards or carrier rules. Third-party standards are referenced, not reproduced. This package contains reusable source files and editorial workflow aids. Repository publication does not imply acceptance by any external directory.
