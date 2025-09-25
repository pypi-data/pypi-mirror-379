import pyenzyme as pe

doc = pe.EnzymeMLDocument(
    name="Test Document",
    description="Test document for verifying the conversion of EnzymeML to Calipytion",
)

NADH = doc.add_to_small_molecules(
    id="NADH",
    name="NADH",
)

NAD = doc.add_to_small_molecules(
    id="NAD",
    name="NAD",
)


measurement1 = doc.add_to_measurements(
    id="measurement_1",
    name="Measurement 1",
    ph=7.4,
    temperature=25,
    temperature_unit="C",
)

measurement1.add_to_species_data(
    species_id="NADH",
    initial=3.0,
    prepared=200,
    data_type=pe.DataTypes.ABSORBANCE,
    data_unit="mmol/l",
    data=[3.0, 2.0, 1.0, 0.0],
    time=[0.0, 1.0, 2.0, 3.0],
    time_unit="s",
)
measurement1.add_to_species_data(
    species_id="NAD",
    initial=0,
    prepared=0,
    data_type=pe.DataTypes.ABSORBANCE,
    data_unit="mmol/l",
    data=[0.0, 1.0, 2.0, 3.0, 4.0],
    time=[0.0, 1.0, 2.0, 3.0, 4.0],
    time_unit="s",
)

# add second measurement
measurement2 = doc.add_to_measurements(
    id="measurement_2",
    name="Measurement 2",
    ph=7.4,
    temperature=25,
    temperature_unit="C",
)

measurement2.add_to_species_data(
    species_id="NADH",
    initial=3.0,
    prepared=300,
    data_type=pe.DataTypes.ABSORBANCE,
    data_unit="mmol/l",
    data=[5.0, 3.0, 2.0, 1.0],
    time=[0.0, 1.0, 2.0, 3.0],
    time_unit="s",
)
measurement2.add_to_species_data(
    species_id="NAD",
    initial=0,
    prepared=0,
    data_type=pe.DataTypes.ABSORBANCE,
    data_unit="mmol/l",
    data=[0.1, 0.2, 0.3, 0.4, 0.5],
    time=[0.0, 1.0, 2.0, 3.0, 4.0],
    time_unit="s",
)

pe.write_enzymeml(doc, "tests/test_data/enzymeml.json")
