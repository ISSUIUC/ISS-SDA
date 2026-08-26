# SDA Coefficients Repository Instructions 

This repository serves as the archive of common properties and tables for rockets flown by the Illinois Space Society's Spaceshot Team. Enclosed in each folder such as `Aether` or `Cassiopeia`, is a file named `SDA.yaml`. `SDA.yaml` files house the properties required for simulation of rockets for each respective folder/rocket name. 

Please see the following descriptions for instructions of adding a **new rocket**. 




```yaml
<<: *simulation # this is internal 
rocket:
  <<: *simulated_rocket  # this is internal
  stages:

    - booster:
      <<: *simulated_stage  # this is internal
      rocket_body:
        <<: *simulated_rocket_body  # this is internal
        rasaero_lookup_file: RASAero.csv # in this format: "RASAero.csv"  
        length: # Enter the length of the rocket WITHOUT units
        dry_mass:  # Enter the dry mass of the rocket body WITHOUT units
        radius:  # Enter the radius of the rocket body WITHOUT units
        structure_CoM: # [x, 0.0, 0.0] enter the center of mass location relative to the tip WITHOUT units 
        combined_CoM: # [x, 0.0, 0.0] enter the center of mass location relative to the tip WITHOUT units 
        combined_cp: # [x, 0.0, 0.0] enter the center of pressure at launch pad location relative to the tip WITHOUT units 
      motor:
        <<: #  *motor_NAME ex.(*motor_M2500)
      avionics: 
        <<: *MIDAS_MINI # etc 

    - sustainer:
      <<: *simulated_stage  # this is internal
      rocket_body:
        <<: *simulated_rocket_body  # this is internal
        rasaero_lookup_file: RASAero.csv # in this format: "RASAero.csv"  
        length: # Enter the length of the rocket WITHOUT units
        dry_mass:  # Enter the dry mass of the rocket body WITHOUT units
        radius:  # Enter the radius of the rocket body WITHOUT units
        structure_CoM: # [x, 0.0, 0.0] enter the center of mass location relative to the tip WITHOUT units 
        combined_CoM: # [x, 0.0, 0.0] enter the center of mass location relative to the tip WITHOUT units 
        combined_cp: # [x, 0.0, 0.0] enter the center of pressure at launch pad location relative to the tip WITHOUT units 
      motor:
        <<: #  *motor_NAME ex.(*motor_M2500)
      avionics: 
        <<: *MIDAS_MINI # etc 

```


## Units 

- Length:  X
- Dry_mass: X
- Radius: X
- Structure_CoM: X
- Combined_CoM: X
- Combined_cp: X


# Important Notes 

- If rocket is single stage, utilize the `SDA.yaml` housed in `single_stage_template`. 

- Example filled in `SDA.yaml` is provided under `Example_Stargazer`. 

- **For Each Rocket** 
  - 
  - Add a folder with the name of the rocket. 
  - Include a `SDA.yaml` file in the folder. Templates are found in `two_stage_template` or `single_stage_template`. 
  - Include a `RASAero.csv` file in the folder.