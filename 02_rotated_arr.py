def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    start = 0
    size = len(input_list)
    pivot = find_pivot(input_list, start, size - 1, size)
    index = get_index(number, input_list, pivot, size, start, size - 1)
    return index


def find_pivot(arr, start, end, size):
    if size == 0 or size == 1:
        return -1
    mid = (start + end) // 2
    if arr[mid] > arr[mid + 1]:
        return mid
    if arr[start] > arr[mid]:
        end = mid
    else:
        start = mid + 1
    return find_pivot(arr, start, end, size)


def get_index(needle, haystack, offset, size, start, end):
    if size == 0:
        return -1

    if size == 1:
        if haystack[0] == needle:
            return 0
        return -1

    mid = (start + end) // 2

    if haystack[index_in(mid, offset, size)] == needle:
        return index_in(mid, offset, size)

    if start > end:
        return -1

    if haystack[index_in(mid, offset, size)] > needle:
        end = mid - 1
        return get_index(needle, haystack, offset, size, start, end)
    elif haystack[index_in(mid, offset, size)] < needle:
        start = mid + 1
        return get_index(needle, haystack, offset, size, start, end)


def index_in(index, offset, size):
    return (index + (size - offset) - 1) % size


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(
            input_list,
            number) == rotated_array_search(
            input_list,
            number):
        print("Pass")
    else:
        print("Fail")


cases = [[[6, 7, 8, 9, 10, 1, 2, 3, 4], 6],
         [[6, 7, 8, 9, 10, 1, 2, 3, 4], 1],
         [[6, 7, 8, 1, 2, 3, 4], 8],
         [[6, 7, 8, 1, 2, 3, 4], 1],
         [[6, 7, 8, 1, 2, 3, 4], 10],
         [[1], 1],
         [[], 1],
         [[5253910,
           5256135,
           5280283,
           5286818,
           5287744,
           5302076,
           5306201,
           5314191,
           5316150,
           5331052,
           5333465,
           5347240,
           5352376,
           5354894,
           5365308,
           5370901,
           5377788,
           5400955,
           5430558,
           5458550,
           5486328,
           5517137,
           5523105,
           5527859,
           5547809,
           5549115,
           5555162,
           5576138,
           5585744,
           5591758,
           5618666,
           5620183,
           5620348,
           5621731,
           5623192,
           5629426,
           5650041,
           5650145,
           5669650,
           5670653,
           5691465,
           5709875,
           5716912,
           5722062,
           5722320,
           5747758,
           5768192,
           5769681,
           5773675,
           5789018,
           5806020,
           5809626,
           5814923,
           5817330,
           5819672,
           5834278,
           5835862,
           5837353,
           5839339,
           5839860,
           5847058,
           5848044,
           5853552,
           5930669,
           5937772,
           5949598,
           5949947,
           5951018,
           5954172,
           5982836,
           6001460,
           6044859,
           6052978,
           6065031,
           6076198,
           6080785,
           6081251,
           6097906,
           6098466,
           6105218,
           6107085,
           6107114,
           6145845,
           6150531,
           6156464,
           6160506,
           6162734,
           6177837,
           6186499,
           6186745,
           6209730,
           6230039,
           6234665,
           6247936,
           6253803,
           6271812,
           6275856,
           6282830,
           6304111,
           6325605,
           6343005,
           6344250,
           6359696,
           6365592,
           6368651,
           6371715,
           6392708,
           6402682,
           6403178,
           6406838,
           6418460,
           6420182,
           6424369,
           6429933,
           6435032,
           6438240,
           6442568,
           6443096,
           6446316,
           6451430,
           6460483,
           6486468,
           6502851,
           6504038,
           6509691,
           6515313,
           6526452,
           6554487,
           6572198,
           6579128,
           6579155,
           6584478,
           6588014,
           6595127,
           6605445,
           6618547,
           6655689,
           6660820,
           6661851,
           6662340,
           6687642,
           6690964,
           6697603,
           6704246,
           6711703,
           6739646,
           6750978,
           6777612,
           6792019,
           6794294,
           6817570,
           6844638,
           6871338,
           6872165,
           6888333,
           6889265,
           6917454,
           6925502,
           6927069,
           6929477,
           6940316,
           6945326,
           6945821,
           6951531,
           6956325,
           6965726,
           6966845,
           6987456,
           6991278,
           6997865,
           6999066,
           7003349,
           7018807,
           7019225,
           7060796,
           7067613,
           7075235,
           7084698,
           7087705,
           7087764,
           7101765,
           7116582,
           7120765,
           7141024,
           7142971,
           7151176,
           7155589,
           7162523,
           7174419,
           7181940,
           7202711,
           7220700,
           7236079,
           7239567,
           7242816,
           7244559,
           7250342,
           7269009,
           7293871,
           7298843,
           7309424,
           7321662,
           7329073,
           7336309,
           7341732,
           7360386,
           7360949,
           7379458,
           7384553,
           7391418,
           7432996,
           7443165,
           7453591,
           7461349,
           7477171,
           7489065,
           7515442,
           7521181,
           7522964,
           7525422,
           7527717,
           7538549,
           7563047,
           7575443,
           7610897,
           7612652,
           7639402,
           7654600,
           7656950,
           7721006,
           7731165,
           7754332,
           7765417,
           7787237,
           7788765,
           7790393,
           7796532,
           7796954,
           7801981,
           7805514,
           7823052,
           7827999,
           7856756,
           7875032,
           7875452,
           7904398,
           7906434,
           7940188,
           7959281,
           7973724,
           7977034,
           7978151,
           7998658,
           8014743,
           8016494,
           8019207,
           8019311,
           8029865,
           8041180,
           8045329,
           8059632,
           8065512,
           8066357,
           8076068,
           8088642,
           8101497,
           8109971,
           8110205,
           8110906,
           8118147,
           8126803,
           8131810,
           8136573,
           8139470,
           8139775,
           8157377,
           8159262,
           8160541,
           8162160,
           8178986,
           8193009,
           8203337,
           8208077,
           8229501,
           8239128,
           8244250,
           8267594,
           8271464,
           8301499,
           8304487,
           8307874,
           8314566,
           8343176,
           8344286,
           8347133,
           8352588,
           8365880,
           8367388,
           8372036,
           8373743,
           8381944,
           8385556,
           8385716,
           8391586,
           8395240,
           8400730,
           8409732,
           8416422,
           8420111,
           8423728,
           8434730,
           8440053,
           8448917,
           8452230,
           8462108,
           8463037,
           8472378,
           8483180,
           8491969,
           8495926,
           8499324,
           8508103,
           8511992,
           8520543,
           8540327,
           8559815,
           8563317,
           8579524,
           8621022,
           8643180,
           8686590,
           8692950,
           8698566,
           8699872,
           8702109,
           8731689,
           8749927,
           8774397,
           8799004,
           8801571,
           8808498,
           8814858,
           8815152,
           8817798,
           8822693,
           8832737,
           8838031,
           8844236,
           8847106,
           8847241,
           8868017,
           8878741,
           8886355,
           8891783,
           8907620,
           8918366,
           8921403,
           8945184,
           8947870,
           8952665,
           8977008,
           8980160,
           8982248,
           8983867,
           9000089,
           9007239,
           9010052,
           9018673,
           9045284,
           9046094,
           9054784,
           9055430,
           9062869,
           9074516,
           9076703,
           9110895,
           9119202,
           9122394,
           9144730,
           9152458,
           9164000,
           9187921,
           9190017,
           9191711,
           9208526,
           9209622,
           9214465,
           9231492,
           9237589,
           9239735,
           9243999,
           9274290,
           9286651,
           9286930,
           9292750,
           9357237,
           9363977,
           9374962,
           9385479,
           9393952,
           9395171,
           9399327,
           9412230,
           9413785,
           9417080,
           9417169,
           9417557,
           9425739,
           9432398,
           9432629,
           9436178,
           9453343,
           9453640,
           9460783,
           9473319,
           9479761,
           9487138,
           9488109,
           9495291,
           9501625,
           9502915,
           9510733,
           9510775,
           9510810,
           9517959,
           9523359,
           9536743,
           9545745,
           9552526,
           9555572,
           9560658,
           9571946,
           9591693,
           9611091,
           9631256,
           9638688,
           9641251,
           9647730,
           9659487,
           9669736,
           9696220,
           9700025,
           9702197,
           9703723,
           9712132,
           9712405,
           9713156,
           9715702,
           9721213,
           9722726,
           9726286,
           9730096,
           9730359,
           9731744,
           9748297,
           9754588,
           9775693,
           9788853,
           9797195,
           9799196,
           9799682,
           9805929,
           9814198,
           9815157,
           9816214,
           9821267,
           9835828,
           9845740,
           9848024,
           9851198,
           9852061,
           9879333,
           9881672,
           9884853,
           9891513,
           9910442,
           9917426,
           9958649,
           9959118,
           9974162,
           9989047,
           9990271,
           2785,
           3036,
           11666,
           21729,
           21934,
           33680,
           57625,
           69547,
           71860,
           73370,
           82698,
           85312,
           87867,
           90672,
           94815,
           122577,
           145942,
           148549,
           158168,
           176647,
           186235,
           192922,
           209365,
           212093,
           237568,
           249582,
           252635,
           279149,
           316543,
           327944,
           342186,
           364958,
           381310,
           385699,
           386188,
           408830,
           409890,
           416905,
           425722,
           430579,
           444912,
           450123,
           452466,
           455033,
           474276,
           500224,
           501590,
           501710,
           516025,
           520044,
           539524,
           547865,
           550471,
           571879,
           586844,
           589723,
           598399,
           613238,
           620666,
           624507,
           635571,
           636462,
           664276,
           679587,
           699639,
           701505,
           702347,
           720139,
           722392,
           744412,
           759836,
           766410,
           768140,
           770003,
           776708,
           789627,
           813247,
           814187,
           830506,
           848388,
           848861,
           865581,
           872678,
           876905,
           885795,
           897061,
           901532,
           901870,
           912837,
           936650,
           972770,
           982136,
           985307,
           1004420,
           1010011,
           1040241,
           1050370,
           1051624,
           1053292,
           1056704,
           1063348,
           1082372,
           1097857,
           1097935,
           1104962,
           1110869,
           1112052,
           1116917,
           1159979,
           1171552,
           1177033,
           1184510,
           1187291,
           1189931,
           1201728,
           1212658,
           1219441,
           1227494,
           1234625,
           1236542,
           1241480,
           1249308,
           1251853,
           1253031,
           1254083,
           1254784,
           1272146,
           1275202,
           1283388,
           1284055,
           1286595,
           1300535,
           1328733,
           1342988,
           1368486,
           1390552,
           1390633,
           1425724,
           1430809,
           1435680,
           1460134,
           1467292,
           1469442,
           1476897,
           1481468,
           1512041,
           1523458,
           1526666,
           1541067,
           1546786,
           1554941,
           1566925,
           1611780,
           1619351,
           1626386,
           1631147,
           1652292,
           1661612,
           1666868,
           1667681,
           1678818,
           1680238,
           1681445,
           1691443,
           1715254,
           1732833,
           1739564,
           1745081,
           1756551,
           1762565,
           1766363,
           1776689,
           1780040,
           1782351,
           1783688,
           1814673,
           1815971,
           1819974,
           1831584,
           1837513,
           1846349,
           1850225,
           1850968,
           1861724,
           1893134,
           1901391,
           1905529,
           1908785,
           1909893,
           1925288,
           1929198,
           1966466,
           1980234,
           1982706,
           2025455,
           2027521,
           2028869,
           2032017,
           2036491,
           2037178,
           2049980,
           2068103,
           2073177,
           2080511,
           2082498,
           2108788,
           2120788,
           2130535,
           2137457,
           2151042,
           2166041,
           2166492,
           2173163,
           2184154,
           2188538,
           2189755,
           2232646,
           2235636,
           2242011,
           2255423,
           2276954,
           2294419,
           2295551,
           2301034,
           2309091,
           2325099,
           2329824,
           2331954,
           2343701,
           2347037,
           2369747,
           2386223,
           2394102,
           2395936,
           2414858,
           2417946,
           2458867,
           2461685,
           2480271,
           2488076,
           2528530,
           2545969,
           2560502,
           2574675,
           2575823,
           2601926,
           2616792,
           2640588,
           2642025,
           2667775,
           2667855,
           2686180,
           2700037,
           2706900,
           2720150,
           2723602,
           2729572,
           2733673,
           2741006,
           2746761,
           2759976,
           2766917,
           2767111,
           2771109,
           2773046,
           2777775,
           2789093,
           2789830,
           2798077,
           2810760,
           2812267,
           2814001,
           2824091,
           2836684,
           2853496,
           2871608,
           2872160,
           2875373,
           2878972,
           2892512,
           2892746,
           2897606,
           2908166,
           2914273,
           2919241,
           2925078,
           2948111,
           2974254,
           2979474,
           2994843,
           2996841,
           2998255,
           3004966,
           3021671,
           3022704,
           3032100,
           3032227,
           3040757,
           3043067,
           3050050,
           3059920,
           3063470,
           3065682,
           3079491,
           3087221,
           3089625,
           3093359,
           3110191,
           3121590,
           3126713,
           3155068,
           3184398,
           3186922,
           3190241,
           3196989,
           3196990,
           3198021,
           3199316,
           3200959,
           3221392,
           3222689,
           3223838,
           3230301,
           3251617,
           3262684,
           3263027,
           3277088,
           3279827,
           3280802,
           3284748,
           3295840,
           3308224,
           3308532,
           3321627,
           3339046,
           3343760,
           3345149,
           3355028,
           3369863,
           3384809,
           3386339,
           3410462,
           3416166,
           3449738,
           3451576,
           3485215,
           3493203,
           3494344,
           3504977,
           3512697,
           3515244,
           3515637,
           3525080,
           3539696,
           3548743,
           3550462,
           3577612,
           3581532,
           3588359,
           3602730,
           3619820,
           3625253,
           3634621,
           3653479,
           3664422,
           3670855,
           3674637,
           3684162,
           3688609,
           3690282,
           3702733,
           3708136,
           3727039,
           3727341,
           3737130,
           3738701,
           3758911,
           3772464,
           3790249,
           3793456,
           3806060,
           3834511,
           3847092,
           3862952,
           3879926,
           3886733,
           3909086,
           3949265,
           3960486,
           3965067,
           3969078,
           4002470,
           4004448,
           4012460,
           4017015,
           4028408,
           4031525,
           4040215,
           4052397,
           4065038,
           4073580,
           4108628,
           4113352,
           4115175,
           4127053,
           4132042,
           4134263,
           4166244,
           4167335,
           4182283,
           4187618,
           4194154,
           4195684,
           4208719,
           4220276,
           4230546,
           4252373,
           4252378,
           4261907,
           4277748,
           4283018,
           4285296,
           4290188,
           4291541,
           4302240,
           4304442,
           4320631,
           4322194,
           4323127,
           4345942,
           4351380,
           4352989,
           4354154,
           4355215,
           4375825,
           4379348,
           4382404,
           4392371,
           4394499,
           4394932,
           4415233,
           4415456,
           4416998,
           4419793,
           4422428,
           4435623,
           4444311,
           4451281,
           4518740,
           4518977,
           4521016,
           4523709,
           4532155,
           4538737,
           4541407,
           4577688,
           4598955,
           4600479,
           4602865,
           4605674,
           4607771,
           4611616,
           4614474,
           4635809,
           4635934,
           4637352,
           4642966,
           4653624,
           4658028,
           4668754,
           4670757,
           4678028,
           4688744,
           4699950,
           4709062,
           4733498,
           4751323,
           4759479,
           4765041,
           4776533,
           4794328,
           4808019,
           4836629,
           4847662,
           4851246,
           4854537,
           4856966,
           4861358,
           4869628,
           4888689,
           4892298,
           4893199,
           4911424,
           4912550,
           4932418,
           4945392,
           4959268,
           5011994,
           5021006,
           5025189,
           5031664,
           5037372,
           5042046,
           5069803,
           5085078,
           5085738,
           5122434,
           5128939,
           5148956,
           5153501,
           5154970,
           5156911,
           5181390,
           5186610,
           5206237,
           5217902,
           5223733,
           5236495],
          3355028]]

for case in cases:
    test_function(case)
