import json
import math

import pyenzyme as pe
from pytest import approx

from calipytion import Calibrator

# create a mock calibrator
cal_data = {
    "molecule_id": "NADH",
    "molecule_name": "NADH",
    "pubchem_cid": 5893,
    "signals": [0, 1, 2, 3, 4],
    "concentrations": [0, 10, 20, 30, 40],
    "conc_unit": "mmol/l",
}

standard_params = {
    "ph": 7.4,
    "temperature": 25,
    "temp_unit": "C",
}


def test_conversion_of_enzymeml_doc():
    # from devtools import pprint

    with open("tests/test_data/enzymeml.json") as f:
        data = json.load(f)

    doc = pe.EnzymeMLDocument(**data)

    ccal = Calibrator(**cal_data)
    ccal.fit_models()
    ccal.create_standard(model=ccal.models[1], **standard_params)

    ccal.apply_to_enzymeml(doc, extrapolate=False)
    print(doc.measurements[1].species_data[0].data)
    assert doc.measurements[0].species_data[0].data_type == pe.DataTypes.CONCENTRATION
    assert doc.measurements[0].species_data[1].data_type == pe.DataTypes.ABSORBANCE
    assert approx(doc.measurements[0].species_data[0].data, abs=0.1) == [
        30,
        20,
        10,
        0,
    ]
    assert approx(doc.measurements[0].species_data[1].data, abs=0.1) == [
        0.0,
        1.0,
        2.0,
        3.0,
        4.0,
    ]
    assert math.isnan(doc.measurements[1].species_data[0].data[0])
    assert approx(doc.measurements[0].species_data[0].initial, abs=0.01) == 30


def test_conversion_of_enzymeml_doc_extrapolate():
    with open("tests/test_data/enzymeml.json") as f:
        data = json.load(f)

    doc = pe.EnzymeMLDocument(**data)

    ccal = Calibrator(**cal_data)
    ccal.fit_models()
    ccal.create_standard(model=ccal.models[0], **standard_params)

    ccal.apply_to_enzymeml(doc, extrapolate=True)

    assert doc.measurements[1].species_data[0].data[0] == approx(50, abs=0.1)
