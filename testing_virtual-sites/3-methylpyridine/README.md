## Running Alchemical Free Energy Calculations with Virtual Sites in Plato

- How the code works: 

Openmmmd.py is modified to include a function called `assignVirtualSites()` 

This function is called when the molecular system is build, and the property "virtual-sites" is assigned to the first molecule of the system. 

Then SOMD looks for this property during the MD simulation. If there is no such property, it continues as it would normally do. 

If there is a "virtual-site" property, then the vSite is added as a particle with charge and LJ parameters that are defined at `opnemmfrenergyst.cpp`, 
and specifically at lines 3027 - 3036:
```
                custom_non_bonded_params_vs[0] = -0.1000; //charge_start
                custom_non_bonded_params_vs[1] = -0.0000; //charge_end
                custom_non_bonded_params_vs[2] = 0.00000 * OpenMM::KJPerKcal; //epsilon_start
                custom_non_bonded_params_vs[3] = 0.00000 * OpenMM::KJPerKcal; //epsilon_end
                custom_non_bonded_params_vs[4] = 1.00000 * OpenMM::NmPerAngstrom; //sigma_start
                custom_non_bonded_params_vs[5] = 1.00000 * OpenMM::NmPerAngstrom; //sigma_end
                custom_non_bonded_params_vs[6] = 0.0; //isHard
                custom_non_bonded_params_vs[7] = 1.0; //isTodummy
                custom_non_bonded_params_vs[8] = 0.0; //isFromdummy
                custom_non_bonded_params_vs[9] = 0.0; //isSolventProtein
```
and also at lines 3188 - 3196:
```
            p_vs_params[0] = -0.10;
            p_vs_params[1] = -0.00;
            p_vs_params[2] = 0.00;
            p_vs_params[3] = 0.00;
            p_vs_params[4] = 1.00;
            p_vs_params[5] = 1.00;
            p_vs_params[6] = 0;
            p_vs_params[7] = 1;
            p_vs_params[8]= 0;
```
Then sire must be compiled again.
The folders for the sire installation are at:
`/export/users/sofia/Software/sire_vs/Sire`
The name of the application should be `/export/users/sofia/sire-vs.app`

- Tips: 

Sire must be compiled every time the charge of the virtual site changes *AND* every time we change from the discharge to the vanish leg, as at the vanish leg, the initial charge of the vSite should be 0, something that we also change manually. 



