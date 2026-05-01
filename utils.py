import pandas as pd

def prepare_data(raw_data) -> pd.DataFrame:
  raw_data = pd.read_csv(raw_data, skiprows=1)
  fix_columns = raw_data.copy()
  raw_data = raw_data.fillna(0)
  column_names = []

  for index, item in enumerate(fix_columns.columns):
    unit = fix_columns[item].iloc[0]
    if "Unnamed" in item:
        column_names.append(f"{fix_columns.columns[index-1]} ({unit})")
    else:
        column_names.append(f'{item} ({unit})')

  fix_columns.columns = column_names
  fix_type = fix_columns.drop([0]).reset_index(drop=True).copy()

  for item in fix_type.columns:
    if not item == "Fraction (Fraction)":
      fix_type[item] = pd.to_numeric(fix_type[item])

  if "Injection (ml)" in fix_type.columns and "Fraction (ml)" in fix_type.columns:
    injection_value = fix_type.iloc[0]["Injection (ml)"]
    fix_type["Fraction (ml)"] = fix_type["Fraction (ml)"] - injection_value

  data = fix_type.copy()
  return data
