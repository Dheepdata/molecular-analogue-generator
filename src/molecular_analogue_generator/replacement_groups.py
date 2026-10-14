replacement_groups = {

    # ============================================================
    # 1. HYDROGEN / ALKYL GROUPS
    # ============================================================
    "alkyl": {
        "methyl": "[*:1]C",
        "ethyl": "[*:1]CC",
        "n_propyl": "[*:1]CCC",
        "n_butyl": "[*:1]CCCC",
        "n_pentyl": "[*:1]CCCCC",
        "n_hexyl": "[*:1]CCCCCC",

        "isopropyl": "[*:1]C(C)C",
        "isobutyl": "[*:1]CC(C)C",
        "sec_butyl": "[*:1]C(C)CC",
        "tert_butyl": "[*:1]C(C)(C)C",

        "neopentyl": "[*:1]CC(C)(C)C",
        "2_methylbutyl": "[*:1]CC(C)CC",
        "3_methylbutyl": "[*:1]CCC(C)C",
    },


    # ============================================================
    # 2. CYCLOALKYL GROUPS
    # ============================================================
    "cycloalkyl": {
        "cyclopropyl": "[*:1]C1CC1",
        "cyclobutyl": "[*:1]C1CCC1",
        "cyclopentyl": "[*:1]C1CCCC1",
        "cyclohexyl": "[*:1]C1CCCCC1",
        "cycloheptyl": "[*:1]C1CCCCCC1",
        "cyclooctyl": "[*:1]C1CCCCCCC1",

        "cyclopropylmethyl": "[*:1]CC1CC1",
        "cyclobutylmethyl": "[*:1]CC1CCC1",
        "cyclopentylmethyl": "[*:1]CC1CCCC1",
        "cyclohexylmethyl": "[*:1]CC1CCCCC1",
    },


    # ============================================================
    # 3. ALKENYL / ALKYNYL GROUPS
    # ============================================================
    "alkenyl_alkynyl": {
        "vinyl": "[*:1]C=C",
        "allyl": "[*:1]CC=C",
        "propenyl": "[*:1]C=CC",
        "isopropenyl": "[*:1]C(C)=C",
        "butenyl": "[*:1]CCC=C",

        "ethynyl": "[*:1]C#C",
        "propynyl": "[*:1]CC#C",
        "butynyl": "[*:1]CCC#C",
    },


    # ============================================================
    # 4. HALOGENS
    # ============================================================
    "halogens": {
        "fluoro": "[*:1]F",
        "chloro": "[*:1]Cl",
        "bromo": "[*:1]Br",
        "iodo": "[*:1]I",
    },


    # ============================================================
    # 5. FLUOROALKYL GROUPS
    # ============================================================
    "fluoroalkyl": {
        "fluoromethyl": "[*:1]CF",
        "difluoromethyl": "[*:1]C(F)F",
        "trifluoromethyl": "[*:1]C(F)(F)F",

        "2_fluoroethyl": "[*:1]CCF",
        "2_difluoroethyl": "[*:1]CC(F)F",
        "2_trifluoroethyl": "[*:1]CC(F)(F)F",

        "pentafluoroethyl": "[*:1]C(F)(F)C(F)(F)F",
    },


    # ============================================================
    # 6. ALKOXY GROUPS
    # ============================================================
    "alkoxy": {
        "methoxy": "[*:1]OC",
        "ethoxy": "[*:1]OCC",
        "n_propoxy": "[*:1]OCCC",
        "isopropoxy": "[*:1]OC(C)C",
        "n_butoxy": "[*:1]OCCCC",
        "isobutoxy": "[*:1]OCC(C)C",
        "tert_butoxy": "[*:1]OC(C)(C)C",

        "cyclopropoxy": "[*:1]OC1CC1",
        "cyclobutoxy": "[*:1]OC1CCC1",
        "cyclopentoxy": "[*:1]OC1CCCC1",
        "cyclohexoxy": "[*:1]OC1CCCCC1",
    },


    # ============================================================
    # 7. FLUOROALKOXY
    # ============================================================
    "fluoroalkoxy": {
        "difluoromethoxy": "[*:1]OC(F)F",
        "trifluoromethoxy": "[*:1]OC(F)(F)F",
        "2_fluoroethoxy": "[*:1]OCCF",
        "2_difluoroethoxy": "[*:1]OCC(F)F",
    },


    # ============================================================
    # 8. HYDROXY / OXYGEN GROUPS
    # ============================================================
    "oxygen": {
        "hydroxy": "[*:1]O",
        "hydroxymethyl": "[*:1]CO",
        "methoxymethyl": "[*:1]COC",
        "ethoxymethyl": "[*:1]COCC",

        "acetoxy": "[*:1]OC(C)=O",
        "formyloxy": "[*:1]OC=O",
    },


    # ============================================================
    # 9. AMINE GROUPS
    # ============================================================
    "amines": {
        "amino": "[*:1]N",
        "methylamino": "[*:1]NC",
        "ethylamino": "[*:1]NCC",
        "propylamino": "[*:1]NCCC",
        "isopropylamino": "[*:1]NC(C)C",

        "dimethylamino": "[*:1]N(C)C",
        "diethylamino": "[*:1]N(CC)CC",
        "ethylmethylamino": "[*:1]N(C)CC",

        "cyclopropylamino": "[*:1]NC1CC1",
        "cyclobutylamino": "[*:1]NC1CCC1",
        "cyclopentylamino": "[*:1]NC1CCCC1",
        "cyclohexylamino": "[*:1]NC1CCCCC1",
    },


    # ============================================================
    # 10. AMIDES
    # ============================================================
    "amides": {
        "carboxamide": "[*:1]C(=O)N",
        "N_methylamide": "[*:1]C(=O)NC",
        "N_ethylamide": "[*:1]C(=O)NCC",
        "N_isopropylamide": "[*:1]C(=O)NC(C)C",
        "N,N_dimethylamide": "[*:1]C(=O)N(C)C",
        "N,N_diethylamide": "[*:1]C(=O)N(CC)CC",

        "N_cyclopropylamide": "[*:1]C(=O)NC1CC1",
        "N_cyclohexylamide": "[*:1]C(=O)NC1CCCCC1",
    },


    # ============================================================
    # 11. CARBONYL / ESTER GROUPS
    # ============================================================
    "carbonyl": {
        "formyl": "[*:1]C=O",
        "acetyl": "[*:1]C(C)=O",
        "propionyl": "[*:1]C(=O)CC",
        "butyryl": "[*:1]C(=O)CCC",

        "methyl_ester": "[*:1]C(=O)OC",
        "ethyl_ester": "[*:1]C(=O)OCC",
        "isopropyl_ester": "[*:1]C(=O)OC(C)C",

        "carboxylic_acid": "[*:1]C(=O)O",
    },


    # ============================================================
    # 12. NITRILE / CYANO
    # ============================================================
    "nitrile": {
        "cyano": "[*:1]C#N",
        "cyanomethyl": "[*:1]CC#N",
    },


    # ============================================================
    # 13. SULFUR GROUPS
    # ============================================================
    "sulfur": {
        "thiol": "[*:1]S",
        "methylthio": "[*:1]SC",
        "ethylthio": "[*:1]SCC",
        "propylthio": "[*:1]SCCC",

        "methylsulfoxide": "[*:1]S(=O)C",
        "ethylsulfoxide": "[*:1]S(=O)CC",

        "methylsulfone": "[*:1]S(=O)(=O)C",
        "ethylsulfone": "[*:1]S(=O)(=O)CC",

        "sulfonamide": "[*:1]S(=O)(=O)N",
        "N_methylsulfonamide": "[*:1]S(=O)(=O)NC",
        "N_ethylsulfonamide": "[*:1]S(=O)(=O)NCC",
        "N_N_dimethylsulfonamide": "[*:1]S(=O)(=O)N(C)C",
    },


    # ============================================================
    # 14. PHENYL / BENZYL
    # ============================================================
    "phenyl": {
        "phenyl": "[*:1]c1ccccc1",

        "benzyl": "[*:1]Cc1ccccc1",

        "tolyl": "[*:1]c1ccc(C)cc1",
        "anisyl": "[*:1]c1ccc(OC)cc1",

        "phenoxy": "[*:1]Oc1ccccc1",
        "phenethyl": "[*:1]CCc1ccccc1",
        "phenylpropyl": "[*:1]CCCc1ccccc1",
    },


    # ============================================================
    # 15. HALOPHENYL GROUPS
    # ============================================================
    "halophenyl": {
        "2_fluorophenyl": "[*:1]c1ccccc1F",
        "3_fluorophenyl": "[*:1]c1cccc(F)c1",
        "4_fluorophenyl": "[*:1]c1ccc(F)cc1",

        "2_chlorophenyl": "[*:1]c1ccccc1Cl",
        "3_chlorophenyl": "[*:1]c1cccc(Cl)c1",
        "4_chlorophenyl": "[*:1]c1ccc(Cl)cc1",

        "2_bromophenyl": "[*:1]c1ccccc1Br",
        "3_bromophenyl": "[*:1]c1cccc(Br)c1",
        "4_bromophenyl": "[*:1]c1ccc(Br)cc1",
    },


    # ============================================================
    # 16. SUBSTITUTED PHENYL
    # ============================================================
    "substituted_phenyl": {
        "2_methylphenyl": "[*:1]c1ccccc1C",
        "3_methylphenyl": "[*:1]c1cccc(C)c1",
        "4_methylphenyl": "[*:1]c1ccc(C)cc1",

        "2_methoxyphenyl": "[*:1]c1ccccc1OC",
        "3_methoxyphenyl": "[*:1]c1cccc(OC)c1",
        "4_methoxyphenyl": "[*:1]c1ccc(OC)cc1",

        "2_hydroxyphenyl": "[*:1]c1ccccc1O",
        "3_hydroxyphenyl": "[*:1]c1cccc(O)c1",
        "4_hydroxyphenyl": "[*:1]c1ccc(O)cc1",

        "2_trifluoromethylphenyl": "[*:1]c1ccccc1C(F)(F)F",
        "3_trifluoromethylphenyl": "[*:1]c1cccc(C(F)(F)F)c1",
        "4_trifluoromethylphenyl": "[*:1]c1ccc(C(F)(F)F)cc1",

        "2_aminophenyl": "[*:1]c1ccccc1N",
        "3_aminophenyl": "[*:1]c1cccc(N)c1",
        "4_aminophenyl": "[*:1]c1ccc(N)cc1",
    },


    # ============================================================
    # 17. PYRIDYL GROUPS
    # ============================================================
    "pyridyl": {
        "2_pyridyl": "[*:1]c1ccccn1",
        "3_pyridyl": "[*:1]c1cccnc1",
        "4_pyridyl": "[*:1]c1ccncc1",
    },


    # ============================================================
    # 18. PYRIMIDINYL / PYRAZINYL / PYRIDAZINYL
    # ============================================================
    "diazines": {
        "2_pyrimidinyl": "[*:1]c1nccnc1",
        "4_pyrimidinyl": "[*:1]c1ncc(nc1)",
        "2_pyrazinyl": "[*:1]c1cnccn1",
        "2_pyridazinyl": "[*:1]c1nnccc1",
    },


    # ============================================================
    # 19. FIVE-MEMBERED HETEROAROMATICS
    # ============================================================
    "five_membered_heteroaryl": {
        "2_furyl": "[*:1]c1ccoc1",
        "3_furyl": "[*:1]c1occc1",

        "2_thienyl": "[*:1]c1ccsc1",
        "3_thienyl": "[*:1]c1sccc1",

        "2_thiazolyl": "[*:1]c1ncsc1",
        "2_oxazolyl": "[*:1]c1ncco1",

        "2_imidazolyl": "[*:1]c1ncc[nH]1",
        "2_pyrazolyl": "[*:1]c1n[nH]cc1",

        "isoxazolyl": "[*:1]c1nocc1",
        "isothiazolyl": "[*:1]c1nscc1",
    },


    # ============================================================
    # 20. SATURATED HETEROCYCLES
    # ============================================================
    "saturated_heterocycles": {
        "morpholine": "[*:1]N1CCOCC1",
        "piperidine": "[*:1]N1CCCCC1",
        "pyrrolidine": "[*:1]N1CCCC1",
        "azetidine": "[*:1]N1CCC1",

        "tetrahydrofuran": "[*:1]C1CCOC1",
        "tetrahydropyran": "[*:1]C1CCOCC1",

        "piperazine": "[*:1]N1CCNCC1",
        "N_methylpiperazine": "[*:1]N1CCN(C)CC1",

        "imidazolidine": "[*:1]N1CCNC1",
        "oxazolidine": "[*:1]N1CCOC1",
    },


    # ============================================================
    # 21. UREA / GUANIDINE / RELATED GROUPS
    # ============================================================
    "nitrogen_carbonyl": {
        "urea": "[*:1]NC(=O)N",
        "N_methylurea": "[*:1]NC(=O)NC",
        "N_N_dimethylurea": "[*:1]NC(=O)N(C)C",

        "guanidine": "[*:1]NC(=N)N",
        "N_methylguanidine": "[*:1]NC(=N)NC",

        "hydrazide": "[*:1]C(=O)NN",
    },


    # ============================================================
    # 22. COMMON POLAR / IONIZABLE GROUPS
    # ============================================================
    "polar_groups": {
        "hydroxyl": "[*:1]O",
        "amino": "[*:1]N",
        "hydroxymethyl": "[*:1]CO",
        "aminomethyl": "[*:1]CN",
        "dimethylaminomethyl": "[*:1]CN(C)C",

        "nitro": "[*:1][N+](=O)[O-]",
        "nitroso": "[*:1]N=O",

        "sulfonamide": "[*:1]S(=O)(=O)N",
        "sulfonic_acid": "[*:1]S(=O)(=O)O",
    },


    # ============================================================
    # 23. BIOISOSTERIC / MEDICINAL-CHEMISTRY GROUPS
    # ============================================================
    "bioisosteres": {
        "tetrazole": "[*:1]c1nnn[nH]1",
        "1_2_4_triazole": "[*:1]c1nnc[nH]1",
        "1_2_3_triazole": "[*:1]c1nn[nH]c1",

        "oxadiazole": "[*:1]c1nnco1",
        "thiadiazole": "[*:1]c1nncs1",

        "imidazole": "[*:1]c1ncc[nH]1",
        "pyrazole": "[*:1]c1n[nH]cc1",
    },
}
