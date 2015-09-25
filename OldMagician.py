# Google Code Jam
# Practice Contests
# Practice Contest
# Problem A. Old Magician

import random

inputTestCases = [[0 for x in range(2)] for x in range(1000)] 
resultWhite = 0
resultBlack = 0

def InitializeInputTestCases():
    global inputTestCases
    inputTestCases[0] = [3, 6]
    inputTestCases[1] = [3, 1]
    inputTestCases[2] = [691, 731]
    inputTestCases[3] = [19, 59]
    inputTestCases[4] = [150, 818]
    inputTestCases[5] = [718, 827]
    inputTestCases[6] = [1000, 1000]
    inputTestCases[7] = [593, 121]
    inputTestCases[8] = [820, 894]
    inputTestCases[9] = [494, 795]
    inputTestCases[10] = [930, 406]
    inputTestCases[11] = [620, 135]
    inputTestCases[12] = [176, 308]
    inputTestCases[13] = [67, 634]
    inputTestCases[14] = [925, 985]
    inputTestCases[15] = [892, 670]
    inputTestCases[16] = [875, 206]
    inputTestCases[17] = [946, 994]
    inputTestCases[18] = [182, 64]
    inputTestCases[19] = [934, 570]
    inputTestCases[20] = [829, 102]
    inputTestCases[21] = [989, 236]
    inputTestCases[22] = [316, 581]
    inputTestCases[23] = [283, 562]
    inputTestCases[24] = [608, 982]
    inputTestCases[25] = [366, 302]
    inputTestCases[26] = [206, 929]
    inputTestCases[27] = [821, 673]
    inputTestCases[28] = [549, 583]
    inputTestCases[29] = [842, 355]
    inputTestCases[30] = [7, 166]
    inputTestCases[31] = [73, 707]
    inputTestCases[32] = [158, 311]
    inputTestCases[33] = [548, 182]
    inputTestCases[34] = [296, 61]
    inputTestCases[35] = [202, 126]
    inputTestCases[36] = [90, 900]
    inputTestCases[37] = [430, 140]
    inputTestCases[38] = [824, 153]
    inputTestCases[39] = [100, 528]
    inputTestCases[40] = [114, 24]
    inputTestCases[41] = [943, 346]
    inputTestCases[42] = [85, 567]
    inputTestCases[43] = [786, 728]
    inputTestCases[44] = [330, 891]
    inputTestCases[45] = [496, 788]
    inputTestCases[46] = [683, 856]
    inputTestCases[47] = [820, 373]
    inputTestCases[48] = [832, 89]
    inputTestCases[49] = [472, 391]
    inputTestCases[50] = [468, 343]
    inputTestCases[51] = [138, 857]
    inputTestCases[52] = [727, 611]
    inputTestCases[53] = [806, 963]
    inputTestCases[54] = [149, 169]
    inputTestCases[55] = [393, 611]
    inputTestCases[56] = [966, 654]
    inputTestCases[57] = [322, 247]
    inputTestCases[58] = [870, 9]
    inputTestCases[59] = [925, 937]
    inputTestCases[60] = [476, 387]
    inputTestCases[61] = [292, 897]
    inputTestCases[62] = [576, 797]
    inputTestCases[63] = [622, 678]
    inputTestCases[64] = [255, 927]
    inputTestCases[65] = [940, 918]
    inputTestCases[66] = [807, 342]
    inputTestCases[67] = [818, 40]
    inputTestCases[68] = [425, 643]
    inputTestCases[69] = [401, 641]
    inputTestCases[70] = [999, 441]
    inputTestCases[71] = [862, 864]
    inputTestCases[72] = [423, 707]
    inputTestCases[73] = [308, 645]
    inputTestCases[74] = [564, 161]
    inputTestCases[75] = [853, 766]
    inputTestCases[76] = [492, 602]
    inputTestCases[77] = [36, 767]
    inputTestCases[78] = [828, 946]
    inputTestCases[79] = [637, 476]
    inputTestCases[80] = [224, 291]
    inputTestCases[81] = [369, 110]
    inputTestCases[82] = [919, 746]
    inputTestCases[83] = [99, 574]
    inputTestCases[84] = [889, 805]
    inputTestCases[85] = [962, 526]
    inputTestCases[86] = [91, 723]
    inputTestCases[87] = [343, 788]
    inputTestCases[88] = [718, 643]
    inputTestCases[89] = [576, 129]
    inputTestCases[90] = [134, 483]
    inputTestCases[91] = [19, 784]
    inputTestCases[92] = [753, 523]
    inputTestCases[93] = [479, 146]
    inputTestCases[94] = [47, 228]
    inputTestCases[95] = [113, 419]
    inputTestCases[96] = [963, 46]
    inputTestCases[97] = [5, 177]
    inputTestCases[98] = [203, 235]
    inputTestCases[99] = [675, 633]
    inputTestCases[100] = [91, 62]
    inputTestCases[101] = [897, 94]
    inputTestCases[102] = [419, 51]
    inputTestCases[103] = [86, 661]
    inputTestCases[104] = [48, 647]
    inputTestCases[105] = [980, 939]
    inputTestCases[106] = [508, 243]
    inputTestCases[107] = [989, 376]
    inputTestCases[108] = [897, 890]
    inputTestCases[109] = [172, 155]
    inputTestCases[110] = [111, 845]
    inputTestCases[111] = [553, 830]
    inputTestCases[112] = [882, 506]
    inputTestCases[113] = [658, 315]
    inputTestCases[114] = [190, 593]
    inputTestCases[115] = [939, 919]
    inputTestCases[116] = [2, 443]
    inputTestCases[117] = [504, 53]
    inputTestCases[118] = [492, 102]
    inputTestCases[119] = [989, 728]
    inputTestCases[120] = [63, 799]
    inputTestCases[121] = [600, 301]
    inputTestCases[122] = [852, 217]
    inputTestCases[123] = [347, 555]
    inputTestCases[124] = [775, 143]
    inputTestCases[125] = [144, 609]
    inputTestCases[126] = [636, 85]
    inputTestCases[127] = [505, 244]
    inputTestCases[128] = [341, 954]
    inputTestCases[129] = [409, 93]
    inputTestCases[130] = [519, 313]
    inputTestCases[131] = [688, 65]
    inputTestCases[132] = [962, 904]
    inputTestCases[133] = [679, 126]
    inputTestCases[134] = [515, 345]
    inputTestCases[135] = [114, 196]
    inputTestCases[136] = [834, 873]
    inputTestCases[137] = [14, 577]
    inputTestCases[138] = [343, 704]
    inputTestCases[139] = [460, 578]
    inputTestCases[140] = [609, 728]
    inputTestCases[141] = [48, 793]
    inputTestCases[142] = [145, 41]
    inputTestCases[143] = [745, 872]
    inputTestCases[144] = [237, 833]
    inputTestCases[145] = [123, 946]
    inputTestCases[146] = [109, 300]
    inputTestCases[147] = [570, 267]
    inputTestCases[148] = [580, 765]
    inputTestCases[149] = [686, 222]
    inputTestCases[150] = [638, 640]
    inputTestCases[151] = [545, 999]
    inputTestCases[152] = [935, 441]
    inputTestCases[153] = [420, 409]
    inputTestCases[154] = [525, 508]
    inputTestCases[155] = [536, 338]
    inputTestCases[156] = [27, 62]
    inputTestCases[157] = [977, 607]
    inputTestCases[158] = [498, 744]
    inputTestCases[159] = [502, 874]
    inputTestCases[160] = [532, 578]
    inputTestCases[161] = [829, 939]
    inputTestCases[162] = [553, 205]
    inputTestCases[163] = [881, 588]
    inputTestCases[164] = [120, 734]
    inputTestCases[165] = [639, 173]
    inputTestCases[166] = [235, 348]
    inputTestCases[167] = [972, 884]
    inputTestCases[168] = [452, 697]
    inputTestCases[169] = [255, 828]
    inputTestCases[170] = [822, 140]
    inputTestCases[171] = [802, 954]
    inputTestCases[172] = [505, 159]
    inputTestCases[173] = [633, 71]
    inputTestCases[174] = [812, 245]
    inputTestCases[175] = [583, 318]
    inputTestCases[176] = [228, 8]
    inputTestCases[177] = [348, 649]
    inputTestCases[178] = [152, 732]
    inputTestCases[179] = [13, 912]
    inputTestCases[180] = [531, 247]
    inputTestCases[181] = [654, 514]
    inputTestCases[182] = [699, 906]
    inputTestCases[183] = [240, 632]
    inputTestCases[184] = [248, 224]
    inputTestCases[185] = [592, 314]
    inputTestCases[186] = [573, 259]
    inputTestCases[187] = [284, 78]
    inputTestCases[188] = [298, 416]
    inputTestCases[189] = [138, 476]
    inputTestCases[190] = [309, 90]
    inputTestCases[191] = [705, 952]
    inputTestCases[192] = [669, 688]
    inputTestCases[193] = [112, 563]
    inputTestCases[194] = [802, 394]
    inputTestCases[195] = [481, 649]
    inputTestCases[196] = [827, 409]
    inputTestCases[197] = [762, 957]
    inputTestCases[198] = [484, 724]
    inputTestCases[199] = [477, 543]
    inputTestCases[200] = [857, 26]
    inputTestCases[201] = [509, 900]
    inputTestCases[202] = [929, 717]
    inputTestCases[203] = [458, 610]
    inputTestCases[204] = [141, 965]
    inputTestCases[205] = [174, 725]
    inputTestCases[206] = [232, 158]
    inputTestCases[207] = [817, 653]
    inputTestCases[208] = [720, 830]
    inputTestCases[209] = [55, 925]
    inputTestCases[210] = [508, 217]
    inputTestCases[211] = [94, 213]
    inputTestCases[212] = [721, 908]
    inputTestCases[213] = [707, 430]
    inputTestCases[214] = [999, 0]
    inputTestCases[215] = [702, 979]
    inputTestCases[216] = [980, 888]
    inputTestCases[217] = [865, 268]
    inputTestCases[218] = [512, 570]
    inputTestCases[219] = [582, 504]
    inputTestCases[220] = [726, 128]
    inputTestCases[221] = [616, 692]
    inputTestCases[222] = [608, 518]
    inputTestCases[223] = [476, 845]
    inputTestCases[224] = [688, 714]
    inputTestCases[225] = [571, 779]
    inputTestCases[226] = [387, 980]
    inputTestCases[227] = [764, 349]
    inputTestCases[228] = [0, 1000]
    inputTestCases[229] = [686, 305]
    inputTestCases[230] = [160, 651]
    inputTestCases[231] = [104, 729]
    inputTestCases[232] = [531, 325]
    inputTestCases[233] = [722, 548]
    inputTestCases[234] = [825, 133]
    inputTestCases[235] = [778, 553]
    inputTestCases[236] = [676, 104]
    inputTestCases[237] = [845, 921]
    inputTestCases[238] = [410, 576]
    inputTestCases[239] = [607, 817]
    inputTestCases[240] = [547, 12]
    inputTestCases[241] = [155, 615]
    inputTestCases[242] = [886, 827]
    inputTestCases[243] = [150, 498]
    inputTestCases[244] = [411, 762]
    inputTestCases[245] = [164, 475]
    inputTestCases[246] = [50, 404]
    inputTestCases[247] = [137, 864]
    inputTestCases[248] = [271, 764]
    inputTestCases[249] = [898, 451]
    inputTestCases[250] = [894, 840]
    inputTestCases[251] = [45, 750]
    inputTestCases[252] = [278, 369]
    inputTestCases[253] = [269, 774]
    inputTestCases[254] = [659, 955]
    inputTestCases[255] = [138, 13]
    inputTestCases[256] = [293, 637]
    inputTestCases[257] = [46, 997]
    inputTestCases[258] = [144, 705]
    inputTestCases[259] = [227, 667]
    inputTestCases[260] = [285, 493]
    inputTestCases[261] = [187, 186]
    inputTestCases[262] = [806, 705]
    inputTestCases[263] = [727, 558]
    inputTestCases[264] = [624, 462]
    inputTestCases[265] = [885, 243]
    inputTestCases[266] = [464, 423]
    inputTestCases[267] = [225, 303]
    inputTestCases[268] = [15, 854]
    inputTestCases[269] = [125, 605]
    inputTestCases[270] = [432, 398]
    inputTestCases[271] = [928, 417]
    inputTestCases[272] = [830, 284]
    inputTestCases[273] = [693, 379]
    inputTestCases[274] = [92, 283]
    inputTestCases[275] = [378, 790]
    inputTestCases[276] = [722, 699]
    inputTestCases[277] = [552, 695]
    inputTestCases[278] = [880, 243]
    inputTestCases[279] = [132, 932]
    inputTestCases[280] = [202, 20]
    inputTestCases[281] = [670, 202]
    inputTestCases[282] = [376, 689]
    inputTestCases[283] = [737, 236]
    inputTestCases[284] = [898, 433]
    inputTestCases[285] = [265, 931]
    inputTestCases[286] = [946, 533]
    inputTestCases[287] = [880, 820]
    inputTestCases[288] = [555, 758]
    inputTestCases[289] = [156, 525]
    inputTestCases[290] = [926, 674]
    inputTestCases[291] = [141, 934]
    inputTestCases[292] = [982, 508]
    inputTestCases[293] = [532, 10]
    inputTestCases[294] = [553, 260]
    inputTestCases[295] = [858, 685]
    inputTestCases[296] = [591, 995]
    inputTestCases[297] = [771, 550]
    inputTestCases[298] = [999, 999]
    inputTestCases[299] = [561, 580]
    inputTestCases[300] = [683, 718]
    inputTestCases[301] = [771, 785]
    inputTestCases[302] = [867, 526]
    inputTestCases[303] = [578, 361]
    inputTestCases[304] = [284, 42]
    inputTestCases[305] = [847, 346]
    inputTestCases[306] = [606, 732]
    inputTestCases[307] = [300, 530]
    inputTestCases[308] = [512, 280]
    inputTestCases[309] = [385, 260]
    inputTestCases[310] = [970, 298]
    inputTestCases[311] = [985, 615]
    inputTestCases[312] = [776, 794]
    inputTestCases[313] = [482, 486]
    inputTestCases[314] = [150, 511]
    inputTestCases[315] = [200, 409]
    inputTestCases[316] = [880, 800]
    inputTestCases[317] = [655, 462]
    inputTestCases[318] = [382, 708]
    inputTestCases[319] = [508, 985]
    inputTestCases[320] = [934, 819]
    inputTestCases[321] = [813, 353]
    inputTestCases[322] = [527, 75]
    inputTestCases[323] = [110, 661]
    inputTestCases[324] = [422, 959]
    inputTestCases[325] = [83, 404]
    inputTestCases[326] = [368, 164]
    inputTestCases[327] = [624, 348]
    inputTestCases[328] = [285, 613]
    inputTestCases[329] = [191, 722]
    inputTestCases[330] = [809, 64]
    inputTestCases[331] = [394, 951]
    inputTestCases[332] = [57, 595]
    inputTestCases[333] = [144, 265]
    inputTestCases[334] = [840, 378]
    inputTestCases[335] = [910, 427]
    inputTestCases[336] = [14, 167]
    inputTestCases[337] = [162, 627]
    inputTestCases[338] = [727, 201]
    inputTestCases[339] = [811, 321]
    inputTestCases[340] = [881, 470]
    inputTestCases[341] = [801, 537]
    inputTestCases[342] = [367, 384]
    inputTestCases[343] = [382, 785]
    inputTestCases[344] = [659, 396]
    inputTestCases[345] = [815, 548]
    inputTestCases[346] = [273, 867]
    inputTestCases[347] = [427, 368]
    inputTestCases[348] = [801, 187]
    inputTestCases[349] = [626, 234]
    inputTestCases[350] = [78, 71]
    inputTestCases[351] = [196, 367]
    inputTestCases[352] = [215, 942]
    inputTestCases[353] = [537, 282]
    inputTestCases[354] = [462, 827]
    inputTestCases[355] = [328, 85]
    inputTestCases[356] = [986, 65]
    inputTestCases[357] = [431, 480]
    inputTestCases[358] = [832, 841]
    inputTestCases[359] = [39, 806]
    inputTestCases[360] = [510, 951]
    inputTestCases[361] = [40, 781]
    inputTestCases[362] = [14, 377]
    inputTestCases[363] = [827, 541]
    inputTestCases[364] = [955, 950]
    inputTestCases[365] = [502, 399]
    inputTestCases[366] = [322, 688]
    inputTestCases[367] = [1, 0]
    inputTestCases[368] = [720, 350]
    inputTestCases[369] = [928, 662]
    inputTestCases[370] = [264, 285]
    inputTestCases[371] = [904, 41]
    inputTestCases[372] = [255, 905]
    inputTestCases[373] = [140, 576]
    inputTestCases[374] = [279, 311]
    inputTestCases[375] = [332, 371]
    inputTestCases[376] = [4, 605]
    inputTestCases[377] = [190, 517]
    inputTestCases[378] = [293, 780]
    inputTestCases[379] = [577, 726]
    inputTestCases[380] = [815, 977]
    inputTestCases[381] = [912, 328]
    inputTestCases[382] = [108, 894]
    inputTestCases[383] = [27, 732]
    inputTestCases[384] = [589, 350]
    inputTestCases[385] = [30, 505]
    inputTestCases[386] = [480, 168]
    inputTestCases[387] = [914, 695]
    inputTestCases[388] = [624, 354]
    inputTestCases[389] = [525, 569]
    inputTestCases[390] = [57, 228]
    inputTestCases[391] = [42, 837]
    inputTestCases[392] = [741, 417]
    inputTestCases[393] = [806, 400]
    inputTestCases[394] = [273, 887]
    inputTestCases[395] = [17, 310]
    inputTestCases[396] = [188, 276]
    inputTestCases[397] = [237, 4]
    inputTestCases[398] = [373, 916]
    inputTestCases[399] = [377, 402]
    inputTestCases[400] = [856, 588]
    inputTestCases[401] = [982, 653]
    inputTestCases[402] = [674, 468]
    inputTestCases[403] = [766, 834]
    inputTestCases[404] = [788, 373]
    inputTestCases[405] = [119, 844]
    inputTestCases[406] = [951, 225]
    inputTestCases[407] = [564, 126]
    inputTestCases[408] = [33, 443]
    inputTestCases[409] = [438, 490]
    inputTestCases[410] = [593, 652]
    inputTestCases[411] = [553, 624]
    inputTestCases[412] = [828, 546]
    inputTestCases[413] = [716, 94]
    inputTestCases[414] = [934, 185]
    inputTestCases[415] = [77, 79]
    inputTestCases[416] = [787, 125]
    inputTestCases[417] = [29, 562]
    inputTestCases[418] = [0, 999]
    inputTestCases[419] = [489, 41]
    inputTestCases[420] = [879, 719]
    inputTestCases[421] = [695, 402]
    inputTestCases[422] = [605, 93]
    inputTestCases[423] = [538, 637]
    inputTestCases[424] = [209, 103]
    inputTestCases[425] = [310, 542]
    inputTestCases[426] = [689, 430]
    inputTestCases[427] = [487, 139]
    inputTestCases[428] = [432, 767]
    inputTestCases[429] = [254, 837]
    inputTestCases[430] = [126, 162]
    inputTestCases[431] = [698, 626]
    inputTestCases[432] = [25, 262]
    inputTestCases[433] = [782, 743]
    inputTestCases[434] = [544, 41]
    inputTestCases[435] = [542, 232]
    inputTestCases[436] = [783, 569]
    inputTestCases[437] = [168, 755]
    inputTestCases[438] = [366, 604]
    inputTestCases[439] = [692, 567]
    inputTestCases[440] = [37, 76]
    inputTestCases[441] = [646, 196]
    inputTestCases[442] = [691, 234]
    inputTestCases[443] = [64, 456]
    inputTestCases[444] = [531, 441]
    inputTestCases[445] = [414, 434]
    inputTestCases[446] = [476, 63]
    inputTestCases[447] = [852, 18]
    inputTestCases[448] = [255, 513]
    inputTestCases[449] = [848, 592]
    inputTestCases[450] = [432, 668]
    inputTestCases[451] = [912, 830]
    inputTestCases[452] = [857, 453]
    inputTestCases[453] = [665, 657]
    inputTestCases[454] = [457, 535]
    inputTestCases[455] = [24, 25]
    inputTestCases[456] = [497, 1]
    inputTestCases[457] = [336, 811]
    inputTestCases[458] = [663, 291]
    inputTestCases[459] = [810, 34]
    inputTestCases[460] = [490, 620]
    inputTestCases[461] = [178, 111]
    inputTestCases[462] = [599, 860]
    inputTestCases[463] = [684, 586]
    inputTestCases[464] = [434, 24]
    inputTestCases[465] = [518, 858]
    inputTestCases[466] = [358, 987]
    inputTestCases[467] = [159, 967]
    inputTestCases[468] = [457, 79]
    inputTestCases[469] = [808, 308]
    inputTestCases[470] = [154, 465]
    inputTestCases[471] = [659, 124]
    inputTestCases[472] = [162, 785]
    inputTestCases[473] = [394, 679]
    inputTestCases[474] = [818, 118]
    inputTestCases[475] = [498, 387]
    inputTestCases[476] = [263, 615]
    inputTestCases[477] = [983, 710]
    inputTestCases[478] = [61, 296]
    inputTestCases[479] = [606, 238]
    inputTestCases[480] = [331, 312]
    inputTestCases[481] = [310, 3]
    inputTestCases[482] = [217, 246]
    inputTestCases[483] = [466, 388]
    inputTestCases[484] = [123, 800]
    inputTestCases[485] = [763, 249]
    inputTestCases[486] = [949, 32]
    inputTestCases[487] = [663, 844]
    inputTestCases[488] = [494, 855]
    inputTestCases[489] = [939, 632]
    inputTestCases[490] = [181, 302]
    inputTestCases[491] = [938, 852]
    inputTestCases[492] = [766, 476]
    inputTestCases[493] = [264, 177]
    inputTestCases[494] = [795, 36]
    inputTestCases[495] = [284, 501]
    inputTestCases[496] = [680, 114]
    inputTestCases[497] = [460, 194]
    inputTestCases[498] = [641, 793]
    inputTestCases[499] = [741, 960]
    inputTestCases[500] = [754, 193]
    inputTestCases[501] = [503, 249]
    inputTestCases[502] = [546, 246]
    inputTestCases[503] = [387, 446]
    inputTestCases[504] = [68, 821]
    inputTestCases[505] = [946, 532]
    inputTestCases[506] = [961, 945]
    inputTestCases[507] = [534, 583]
    inputTestCases[508] = [630, 657]
    inputTestCases[509] = [61, 514]
    inputTestCases[510] = [548, 350]
    inputTestCases[511] = [106, 670]
    inputTestCases[512] = [892, 37]
    inputTestCases[513] = [942, 336]
    inputTestCases[514] = [955, 840]
    inputTestCases[515] = [714, 814]
    inputTestCases[516] = [255, 508]
    inputTestCases[517] = [714, 997]
    inputTestCases[518] = [379, 229]
    inputTestCases[519] = [110, 213]
    inputTestCases[520] = [67, 88]
    inputTestCases[521] = [1000, 563]
    inputTestCases[522] = [886, 667]
    inputTestCases[523] = [937, 63]
    inputTestCases[524] = [885, 462]
    inputTestCases[525] = [641, 584]
    inputTestCases[526] = [854, 402]
    inputTestCases[527] = [734, 852]
    inputTestCases[528] = [926, 136]
    inputTestCases[529] = [921, 366]
    inputTestCases[530] = [209, 184]
    inputTestCases[531] = [140, 570]
    inputTestCases[532] = [618, 98]
    inputTestCases[533] = [473, 519]
    inputTestCases[534] = [615, 895]
    inputTestCases[535] = [202, 498]
    inputTestCases[536] = [677, 950]
    inputTestCases[537] = [989, 988]
    inputTestCases[538] = [616, 596]
    inputTestCases[539] = [847, 442]
    inputTestCases[540] = [103, 565]
    inputTestCases[541] = [767, 674]
    inputTestCases[542] = [480, 276]
    inputTestCases[543] = [652, 416]
    inputTestCases[544] = [986, 671]
    inputTestCases[545] = [575, 648]
    inputTestCases[546] = [732, 864]
    inputTestCases[547] = [821, 275]
    inputTestCases[548] = [382, 411]
    inputTestCases[549] = [685, 770]
    inputTestCases[550] = [984, 598]
    inputTestCases[551] = [816, 288]
    inputTestCases[552] = [13, 312]
    inputTestCases[553] = [733, 197]
    inputTestCases[554] = [1000, 999]
    inputTestCases[555] = [401, 262]
    inputTestCases[556] = [890, 767]
    inputTestCases[557] = [183, 414]
    inputTestCases[558] = [415, 560]
    inputTestCases[559] = [131, 831]
    inputTestCases[560] = [806, 358]
    inputTestCases[561] = [906, 486]
    inputTestCases[562] = [898, 99]
    inputTestCases[563] = [784, 733]
    inputTestCases[564] = [752, 64]
    inputTestCases[565] = [634, 44]
    inputTestCases[566] = [542, 745]
    inputTestCases[567] = [170, 2]
    inputTestCases[568] = [8, 600]
    inputTestCases[569] = [642, 221]
    inputTestCases[570] = [761, 336]
    inputTestCases[571] = [661, 488]
    inputTestCases[572] = [361, 130]
    inputTestCases[573] = [393, 520]
    inputTestCases[574] = [450, 370]
    inputTestCases[575] = [176, 189]
    inputTestCases[576] = [985, 980]
    inputTestCases[577] = [63, 578]
    inputTestCases[578] = [750, 347]
    inputTestCases[579] = [787, 134]
    inputTestCases[580] = [351, 67]
    inputTestCases[581] = [87, 365]
    inputTestCases[582] = [19, 539]
    inputTestCases[583] = [616, 861]
    inputTestCases[584] = [590, 364]
    inputTestCases[585] = [903, 724]
    inputTestCases[586] = [36, 254]
    inputTestCases[587] = [696, 141]
    inputTestCases[588] = [634, 641]
    inputTestCases[589] = [282, 72]
    inputTestCases[590] = [607, 553]
    inputTestCases[591] = [586, 783]
    inputTestCases[592] = [42, 36]
    inputTestCases[593] = [591, 288]
    inputTestCases[594] = [820, 615]
    inputTestCases[595] = [8, 824]
    inputTestCases[596] = [173, 96]
    inputTestCases[597] = [426, 843]
    inputTestCases[598] = [380, 473]
    inputTestCases[599] = [346, 549]
    inputTestCases[600] = [13, 118]
    inputTestCases[601] = [387, 659]
    inputTestCases[602] = [302, 126]
    inputTestCases[603] = [368, 788]
    inputTestCases[604] = [92, 465]
    inputTestCases[605] = [392, 514]
    inputTestCases[606] = [657, 354]
    inputTestCases[607] = [541, 259]
    inputTestCases[608] = [16, 350]
    inputTestCases[609] = [67, 300]
    inputTestCases[610] = [312, 771]
    inputTestCases[611] = [589, 102]
    inputTestCases[612] = [133, 428]
    inputTestCases[613] = [644, 366]
    inputTestCases[614] = [982, 758]
    inputTestCases[615] = [453, 62]
    inputTestCases[616] = [141, 18]
    inputTestCases[617] = [864, 497]
    inputTestCases[618] = [174, 695]
    inputTestCases[619] = [566, 32]
    inputTestCases[620] = [86, 874]
    inputTestCases[621] = [74, 601]
    inputTestCases[622] = [7, 151]
    inputTestCases[623] = [739, 857]
    inputTestCases[624] = [704, 513]
    inputTestCases[625] = [146, 959]
    inputTestCases[626] = [640, 653]
    inputTestCases[627] = [851, 796]
    inputTestCases[628] = [846, 843]
    inputTestCases[629] = [981, 262]
    inputTestCases[630] = [334, 310]
    inputTestCases[631] = [57, 558]
    inputTestCases[632] = [816, 817]
    inputTestCases[633] = [886, 998]
    inputTestCases[634] = [165, 393]
    inputTestCases[635] = [774, 72]
    inputTestCases[636] = [212, 525]
    inputTestCases[637] = [345, 924]
    inputTestCases[638] = [694, 758]
    inputTestCases[639] = [997, 965]
    inputTestCases[640] = [845, 230]
    inputTestCases[641] = [847, 365]
    inputTestCases[642] = [69, 683]
    inputTestCases[643] = [408, 819]
    inputTestCases[644] = [619, 202]
    inputTestCases[645] = [373, 382]
    inputTestCases[646] = [992, 398]
    inputTestCases[647] = [431, 584]
    inputTestCases[648] = [548, 710]
    inputTestCases[649] = [714, 891]
    inputTestCases[650] = [130, 422]
    inputTestCases[651] = [223, 942]
    inputTestCases[652] = [170, 742]
    inputTestCases[653] = [78, 657]
    inputTestCases[654] = [818, 402]
    inputTestCases[655] = [2, 977]
    inputTestCases[656] = [947, 576]
    inputTestCases[657] = [818, 770]
    inputTestCases[658] = [632, 698]
    inputTestCases[659] = [451, 590]
    inputTestCases[660] = [808, 18]
    inputTestCases[661] = [620, 492]
    inputTestCases[662] = [168, 854]
    inputTestCases[663] = [296, 133]
    inputTestCases[664] = [670, 820]
    inputTestCases[665] = [355, 417]
    inputTestCases[666] = [22, 748]
    inputTestCases[667] = [619, 875]
    inputTestCases[668] = [702, 436]
    inputTestCases[669] = [12, 748]
    inputTestCases[670] = [732, 273]
    inputTestCases[671] = [256, 357]
    inputTestCases[672] = [550, 634]
    inputTestCases[673] = [292, 0]
    inputTestCases[674] = [204, 551]
    inputTestCases[675] = [601, 918]
    inputTestCases[676] = [325, 439]
    inputTestCases[677] = [684, 142]
    inputTestCases[678] = [313, 683]
    inputTestCases[679] = [72, 162]
    inputTestCases[680] = [663, 813]
    inputTestCases[681] = [214, 417]
    inputTestCases[682] = [55, 6]
    inputTestCases[683] = [401, 153]
    inputTestCases[684] = [932, 273]
    inputTestCases[685] = [268, 878]
    inputTestCases[686] = [467, 310]
    inputTestCases[687] = [470, 736]
    inputTestCases[688] = [483, 685]
    inputTestCases[689] = [58, 928]
    inputTestCases[690] = [748, 548]
    inputTestCases[691] = [954, 308]
    inputTestCases[692] = [937, 516]
    inputTestCases[693] = [339, 798]
    inputTestCases[694] = [419, 399]
    inputTestCases[695] = [917, 179]
    inputTestCases[696] = [22, 371]
    inputTestCases[697] = [63, 264]
    inputTestCases[698] = [450, 851]
    inputTestCases[699] = [297, 149]
    inputTestCases[700] = [87, 2]
    inputTestCases[701] = [876, 824]
    inputTestCases[702] = [136, 437]
    inputTestCases[703] = [776, 997]
    inputTestCases[704] = [5, 943]
    inputTestCases[705] = [944, 863]
    inputTestCases[706] = [759, 449]
    inputTestCases[707] = [440, 6]
    inputTestCases[708] = [539, 573]
    inputTestCases[709] = [180, 548]
    inputTestCases[710] = [909, 555]
    inputTestCases[711] = [722, 58]
    inputTestCases[712] = [383, 97]
    inputTestCases[713] = [879, 463]
    inputTestCases[714] = [999, 925]
    inputTestCases[715] = [45, 156]
    inputTestCases[716] = [508, 259]
    inputTestCases[717] = [968, 866]
    inputTestCases[718] = [848, 314]
    inputTestCases[719] = [50, 435]
    inputTestCases[720] = [45, 649]
    inputTestCases[721] = [127, 730]
    inputTestCases[722] = [989, 831]
    inputTestCases[723] = [513, 388]
    inputTestCases[724] = [603, 804]
    inputTestCases[725] = [806, 904]
    inputTestCases[726] = [946, 24]
    inputTestCases[727] = [952, 465]
    inputTestCases[728] = [565, 160]
    inputTestCases[729] = [668, 316]
    inputTestCases[730] = [732, 405]
    inputTestCases[731] = [469, 894]
    inputTestCases[732] = [213, 257]
    inputTestCases[733] = [677, 227]
    inputTestCases[734] = [573, 776]
    inputTestCases[735] = [928, 777]
    inputTestCases[736] = [672, 398]
    inputTestCases[737] = [244, 766]
    inputTestCases[738] = [751, 356]
    inputTestCases[739] = [536, 672]
    inputTestCases[740] = [311, 231]
    inputTestCases[741] = [62, 369]
    inputTestCases[742] = [666, 896]
    inputTestCases[743] = [31, 799]
    inputTestCases[744] = [136, 87]
    inputTestCases[745] = [778, 546]
    inputTestCases[746] = [356, 151]
    inputTestCases[747] = [973, 905]
    inputTestCases[748] = [716, 693]
    inputTestCases[749] = [690, 676]
    inputTestCases[750] = [76, 299]
    inputTestCases[751] = [324, 246]
    inputTestCases[752] = [5, 769]
    inputTestCases[753] = [768, 439]
    inputTestCases[754] = [962, 587]
    inputTestCases[755] = [666, 85]
    inputTestCases[756] = [10, 461]
    inputTestCases[757] = [402, 607]
    inputTestCases[758] = [435, 95]
    inputTestCases[759] = [406, 594]
    inputTestCases[760] = [9, 618]
    inputTestCases[761] = [55, 371]
    inputTestCases[762] = [521, 25]
    inputTestCases[763] = [883, 113]
    inputTestCases[764] = [611, 795]
    inputTestCases[765] = [558, 642]
    inputTestCases[766] = [571, 991]
    inputTestCases[767] = [474, 532]
    inputTestCases[768] = [871, 112]
    inputTestCases[769] = [887, 458]
    inputTestCases[770] = [444, 627]
    inputTestCases[771] = [165, 301]
    inputTestCases[772] = [468, 193]
    inputTestCases[773] = [906, 494]
    inputTestCases[774] = [43, 265]
    inputTestCases[775] = [480, 468]
    inputTestCases[776] = [591, 460]
    inputTestCases[777] = [346, 152]
    inputTestCases[778] = [881, 193]
    inputTestCases[779] = [896, 90]
    inputTestCases[780] = [453, 698]
    inputTestCases[781] = [371, 849]
    inputTestCases[782] = [545, 450]
    inputTestCases[783] = [535, 294]
    inputTestCases[784] = [261, 746]
    inputTestCases[785] = [56, 40]
    inputTestCases[786] = [639, 879]
    inputTestCases[787] = [526, 89]
    inputTestCases[788] = [50, 6]
    inputTestCases[789] = [364, 499]
    inputTestCases[790] = [0, 1]
    inputTestCases[791] = [689, 429]
    inputTestCases[792] = [95, 516]
    inputTestCases[793] = [478, 718]
    inputTestCases[794] = [110, 729]
    inputTestCases[795] = [735, 966]
    inputTestCases[796] = [152, 533]
    inputTestCases[797] = [986, 931]
    inputTestCases[798] = [909, 286]
    inputTestCases[799] = [272, 189]
    inputTestCases[800] = [166, 839]
    inputTestCases[801] = [586, 589]
    inputTestCases[802] = [238, 41]
    inputTestCases[803] = [56, 743]
    inputTestCases[804] = [272, 713]
    inputTestCases[805] = [821, 876]
    inputTestCases[806] = [856, 843]
    inputTestCases[807] = [77, 519]
    inputTestCases[808] = [601, 1000]
    inputTestCases[809] = [26, 90]
    inputTestCases[810] = [750, 629]
    inputTestCases[811] = [783, 984]
    inputTestCases[812] = [914, 22]
    inputTestCases[813] = [100, 923]
    inputTestCases[814] = [433, 413]
    inputTestCases[815] = [813, 736]
    inputTestCases[816] = [904, 686]
    inputTestCases[817] = [407, 49]
    inputTestCases[818] = [915, 985]
    inputTestCases[819] = [385, 886]
    inputTestCases[820] = [771, 674]
    inputTestCases[821] = [607, 443]
    inputTestCases[822] = [685, 934]
    inputTestCases[823] = [67, 235]
    inputTestCases[824] = [856, 932]
    inputTestCases[825] = [102, 138]
    inputTestCases[826] = [821, 995]
    inputTestCases[827] = [175, 85]
    inputTestCases[828] = [241, 784]
    inputTestCases[829] = [518, 353]
    inputTestCases[830] = [555, 83]
    inputTestCases[831] = [496, 40]
    inputTestCases[832] = [870, 687]
    inputTestCases[833] = [174, 110]
    inputTestCases[834] = [471, 755]
    inputTestCases[835] = [604, 653]
    inputTestCases[836] = [20, 890]
    inputTestCases[837] = [954, 149]
    inputTestCases[838] = [708, 310]
    inputTestCases[839] = [815, 347]
    inputTestCases[840] = [695, 165]
    inputTestCases[841] = [135, 403]
    inputTestCases[842] = [103, 588]
    inputTestCases[843] = [837, 532]
    inputTestCases[844] = [550, 495]
    inputTestCases[845] = [442, 167]
    inputTestCases[846] = [55, 463]
    inputTestCases[847] = [263, 487]
    inputTestCases[848] = [263, 753]
    inputTestCases[849] = [240, 785]
    inputTestCases[850] = [492, 509]
    inputTestCases[851] = [237, 500]
    inputTestCases[852] = [889, 490]
    inputTestCases[853] = [952, 596]
    inputTestCases[854] = [365, 898]
    inputTestCases[855] = [999, 1000]
    inputTestCases[856] = [169, 325]
    inputTestCases[857] = [171, 292]
    inputTestCases[858] = [43, 948]
    inputTestCases[859] = [996, 383]
    inputTestCases[860] = [793, 252]
    inputTestCases[861] = [668, 348]
    inputTestCases[862] = [252, 574]
    inputTestCases[863] = [925, 663]
    inputTestCases[864] = [97, 673]
    inputTestCases[865] = [755, 558]
    inputTestCases[866] = [953, 229]
    inputTestCases[867] = [57, 375]
    inputTestCases[868] = [154, 697]
    inputTestCases[869] = [862, 74]
    inputTestCases[870] = [401, 430]
    inputTestCases[871] = [321, 482]
    inputTestCases[872] = [297, 680]
    inputTestCases[873] = [218, 152]
    inputTestCases[874] = [654, 261]
    inputTestCases[875] = [222, 353]
    inputTestCases[876] = [95, 907]
    inputTestCases[877] = [970, 177]
    inputTestCases[878] = [469, 864]
    inputTestCases[879] = [799, 483]
    inputTestCases[880] = [490, 305]
    inputTestCases[881] = [91, 943]
    inputTestCases[882] = [180, 86]
    inputTestCases[883] = [442, 367]
    inputTestCases[884] = [236, 501]
    inputTestCases[885] = [446, 950]
    inputTestCases[886] = [972, 43]
    inputTestCases[887] = [154, 184]
    inputTestCases[888] = [53, 812]
    inputTestCases[889] = [335, 960]
    inputTestCases[890] = [617, 155]
    inputTestCases[891] = [678, 661]
    inputTestCases[892] = [792, 902]
    inputTestCases[893] = [278, 820]
    inputTestCases[894] = [356, 128]
    inputTestCases[895] = [992, 290]
    inputTestCases[896] = [871, 162]
    inputTestCases[897] = [278, 700]
    inputTestCases[898] = [873, 634]
    inputTestCases[899] = [906, 264]
    inputTestCases[900] = [867, 543]
    inputTestCases[901] = [93, 305]
    inputTestCases[902] = [384, 16]
    inputTestCases[903] = [287, 238]
    inputTestCases[904] = [777, 689]
    inputTestCases[905] = [855, 143]
    inputTestCases[906] = [363, 363]
    inputTestCases[907] = [381, 476]
    inputTestCases[908] = [263, 277]
    inputTestCases[909] = [110, 324]
    inputTestCases[910] = [500, 304]
    inputTestCases[911] = [900, 121]
    inputTestCases[912] = [90, 476]
    inputTestCases[913] = [748, 258]
    inputTestCases[914] = [62, 487]
    inputTestCases[915] = [813, 299]
    inputTestCases[916] = [201, 207]
    inputTestCases[917] = [841, 36]
    inputTestCases[918] = [711, 88]
    inputTestCases[919] = [340, 639]
    inputTestCases[920] = [558, 706]
    inputTestCases[921] = [890, 793]
    inputTestCases[922] = [573, 304]
    inputTestCases[923] = [601, 389]
    inputTestCases[924] = [712, 110]
    inputTestCases[925] = [819, 891]
    inputTestCases[926] = [299, 466]
    inputTestCases[927] = [380, 487]
    inputTestCases[928] = [479, 54]
    inputTestCases[929] = [636, 702]
    inputTestCases[930] = [298, 668]
    inputTestCases[931] = [682, 723]
    inputTestCases[932] = [262, 750]
    inputTestCases[933] = [1000, 0]
    inputTestCases[934] = [483, 678]
    inputTestCases[935] = [767, 338]
    inputTestCases[936] = [984, 657]
    inputTestCases[937] = [68, 429]
    inputTestCases[938] = [395, 337]
    inputTestCases[939] = [527, 584]
    inputTestCases[940] = [234, 200]
    inputTestCases[941] = [694, 499]
    inputTestCases[942] = [255, 901]
    inputTestCases[943] = [7, 701]
    inputTestCases[944] = [874, 945]
    inputTestCases[945] = [110, 832]
    inputTestCases[946] = [559, 255]
    inputTestCases[947] = [928, 67]
    inputTestCases[948] = [279, 776]
    inputTestCases[949] = [833, 755]
    inputTestCases[950] = [740, 223]
    inputTestCases[951] = [261, 850]
    inputTestCases[952] = [777, 127]
    inputTestCases[953] = [305, 738]
    inputTestCases[954] = [469, 421]
    inputTestCases[955] = [492, 81]
    inputTestCases[956] = [564, 126]
    inputTestCases[957] = [442, 195]
    inputTestCases[958] = [760, 642]
    inputTestCases[959] = [805, 161]
    inputTestCases[960] = [726, 644]
    inputTestCases[961] = [579, 542]
    inputTestCases[962] = [708, 343]
    inputTestCases[963] = [557, 134]
    inputTestCases[964] = [875, 963]
    inputTestCases[965] = [76, 990]
    inputTestCases[966] = [680, 256]
    inputTestCases[967] = [52, 864]
    inputTestCases[968] = [315, 718]
    inputTestCases[969] = [719, 711]
    inputTestCases[970] = [929, 928]
    inputTestCases[971] = [907, 751]
    inputTestCases[972] = [774, 220]
    inputTestCases[973] = [512, 157]
    inputTestCases[974] = [190, 737]
    inputTestCases[975] = [553, 733]
    inputTestCases[976] = [564, 753]
    inputTestCases[977] = [462, 673]
    inputTestCases[978] = [260, 812]
    inputTestCases[979] = [234, 32]
    inputTestCases[980] = [660, 803]
    inputTestCases[981] = [804, 347]
    inputTestCases[982] = [533, 243]
    inputTestCases[983] = [851, 365]
    inputTestCases[984] = [620, 526]
    inputTestCases[985] = [521, 676]
    inputTestCases[986] = [141, 834]
    inputTestCases[987] = [534, 954]
    inputTestCases[988] = [778, 197]
    inputTestCases[989] = [310, 213]
    inputTestCases[990] = [357, 257]
    inputTestCases[991] = [895, 101]
    inputTestCases[992] = [624, 610]
    inputTestCases[993] = [689, 319]
    inputTestCases[994] = [987, 856]
    inputTestCases[995] = [237, 290]
    inputTestCases[996] = [16, 748]
    inputTestCases[997] = [4, 222]
    inputTestCases[998] = [914, 608]
    inputTestCases[999] = [194, 922]

def Draw(k, count):
    selection = [0 for x in range(2)]
    for x in range(count - k + 1, count):
        randInt = random.randint(0, count - 1)
        if (randInt in selection): selection.append(randInt)
        else: selection.append(x)
    return selection

def UpdateBalls(balls):
    white = balls[0]
    black = balls[1]
    ballCount = white + black
    
    selection = Draw(2, ballCount)
    if (selection[0] < white and selection[1] < white): 
        newWhite = white - 1
        newBlack = black
    elif (selection[0] >= white and selection[1] >= white):
        newWhite = white + 1
        newBlack = black - 2
    else: 
        newWhite = white - 1
        newBlack = black

    return [newWhite, newBlack]
    
def UpdateUntilLastBall(balls):
    global resultWhite
    global resultBlack
    count = balls[0] + balls[1]
    while (count > 1):
        balls = UpdateBalls(balls)
        count = balls[0] + balls[1]
    if (balls == [1, 0]): resultWhite += 1
    elif (balls == [0, 1]): resultBlack += 1

def ResetCount():
    resultWhite = 0
    resultBlack = 0

def SimulateResult(testCaseNo, count):
    balls = inputTestCases[testCaseNo]
    for x in range(count):
        UpdateUntilLastBall(balls)
    if (resultWhite == count): print("Case #" & testCaseNo & ": " & "WHITE")
    elif: (resultBlack == count): print("Case #" & testCaseNo & ": " & "BLACK")
    else: print("Case #" & testCaseNo & ": " & "UNKNOWN")
    ResetCount()
        
InitializeInputTestCases()
for x in range(1000):
    SimulateResult(x)
