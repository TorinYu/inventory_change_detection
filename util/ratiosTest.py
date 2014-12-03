# -*- coding: utf-8 -*-
import os
import sys

ratios_changed = [
	0,
	0.003861004,
	0.004081633,
	0.006726457,
	0.007936508,
	0.019607843,
	0.025695931,
	0.025974026,
	0.039007092,
	0.04,
	0.041666667,
	0.042553191,
	0.043227666,
	0.046511628,
	0.04784689,
	0.048543689,
	0.051948052,
	0.052631579,
	0.054945055,
	0.062256809,
	0.063953488,
	0.069587629,
	0.082191781,
	0.087087087,
	0.090047393,
	0.095652174,
	0.105363985,
	0.107438017,
	0.110091743,
	0.114678899,
	0.130681818,
	0.132231405,
	0.134328358,
	0.140202703,
	0.148471616,
	0.149812734,
	0.152866242,
	0.158536585,
	0.167286245,
	0.180722892,
	0.182608696,
	0.19266055,
	0.193236715,
	0.197309417,
	0.200598802,
	0.215517241,
	0.218543046,
	0.244623656,
	0.272058824,
	0.28975265,
	0.304761905
]

ratios_unchanged = [
	0,
	0.079470199,
	0.093474427,
	0.107407407,
	0.107784431,
	0.112,
	0.124113475,
	0.142023346,
	0.147286822,
	0.157407407,
	0.158357771,
	0.18490566,
	0.201086957,
	0.204081633,
	0.204737733,
	0.224637681,
	0.228947368,
	0.229591837,
	0.23015873,
	0.247933884,
	0.248868778,
	0.25,
	0.252252252,
	0.256944444,
	0.258215962,
	0.265734266,
	0.266233766,
	0.275362319,
	0.280851064,
	0.28125,
	0.289389068,
	0.289772727,
	0.295744681,
	0.298898072,
	0.299232737,
	0.299435028,
	0.301587302,
	0.306451613,
	0.310160428,
	0.316939891,
	0.317073171,
	0.321100917,
	0.321782178,
	0.325301205,
	0.325966851,
	0.327217125,
	0.336244541,
	0.342465753,
	0.350877193,
	0.400534045,
	0.501845018
]


changed_075 = [
	0.167442,
	0.0661157,
	0.235023,
	0.292857,
	0.107143,
	0.0592885,
	0.104651,
	0.226087,
	0.237288,
	0.210383,
	0.401709,
	0.165217,
	0.177936,
	0.254335,
	0.11985,
	0.269663,
	0.114144,
	0.345411,
	0.297959,
	0.106667,
	0.224138,
	0.29902,
	0.0806794,
	0.248624,
	0.267241,
	0.162011,
	0.304721,
	0.166667,
	0.257143,
	0.281013,
	0.313333,
	0.320359,
	0.257962,
	0.286726,
	0.06621,
	0.292226,
	0.309735,
	0.367816,
	0.398693,
	0.245333,
	0.118182,
	0.103352,
	0.019305,
	0.0609756,
	0.163636,
	0.252252,
	0.173516,
	0.128686,
	0.388679,
	0.394309,
	0.37149,
	0.255076
]

changed_09 = [
	0.516279,
	0.264463,
	0.442396,
	0.575188,
	0.392857,
	0.217391,
	0.360465,
	0.465217,
	0.440678,
	0.442623,
	0.589744,
	0.395652,
	0.41637,
	0.514451,
	0.35206,
	0.513109,
	0.315136,
	0.504831,
	0.457143,
	0.373333,
	0.456897,
	0.54902,
	0.254777,
	0.56422,
	0.508621,
	0.396648,
	0.566524,
	0.490196,
	0.535238,
	0.679928,
	0.526667,
	0.5,
	0.484076,
	0.495575,
	0.3379,
	0.568905,
	0.566372,
	0.609195,
	0.601307,
	0.64,
	0.263636,
	0.418994,
	0.158301,
	0.280488,
	0.412121,
	0.454955,
	0.438356,
	0.302949,
	0.6,
	0.630081,
	0.555076,
	0.555076
]

unchanged_09 = [
	0.582623,
	0.670157,
	0.598425,
	0.582278,
	0.595308,
	0.616197,
	0.635468,
	0.609375,
	0.588517,
	0.616314,
	0.609756,
	0.652411,
	0.617778,
	0.613377,
	0.663239,
	0.698413,
	0.658503,
	0.572277,
	0.623776,
	0.569444,
	0.619772,
	0.432143,
	0.621192,
	0.620991,
	0.651786,
	0.602812,
	0.705628,
	0.581081,
	0.457338,
	0.469136,
	0.701887,
	0.642673,
	0.596667,
	0.656676,
	0.663717,
	0.609959,
	0.63754,
	0.494024,
	0.650538,
	0.507143,
	0.667742,
	0.618834,
	0.530387,
	0.625628,
	0.617424,
	0.587678,
	0.532934,
	0.536585,
	0.645914,
	0.760638,
	0.492647,
	0.492647
]

unchanged_075 = [
	0.408859,
	0.554974,
	0.405512,
	0.45443,
	0.439883,
	0.447183,
	0.438424,
	0.441406,
	0.363636,
	0.444109,
	0.44878,
	0.507776,
	0.457778,
	0.430669,
	0.434447,
	0.428571,
	0.541497,
	0.328713,
	0.462937,
	0.425926,
	0.342205,
	0.239286,
	0.417219,
	0.396501,
	0.4375,
	0.43761,
	0.493506,
	0.418919,
	0.31843,
	0.485185,
	0.581132,
	0.44473,
	0.4,
	0.474114,
	0.460177,
	0.452282,
	0.446602,
	0.330677,
	0.467742,
	0.321429,
	0.503226,
	0.470852,
	0.325967,
	0.432161,
	0.475,
	0.379147,
	0.411377,
	0.333333,
	0.470817,
	0.579787,
	0.479412,
	0.492647
]


def get_paired_images(imgdir):
	pairs = []
	for imgfile in os.listdir(imgdir):
		imgpath = os.path.join(imgdir, imgfile)
		if imgfile.endswith("inbound.jpg"):
			img1 = imgpath
			img2 = os.path.join(imgdir, imgfile.replace("inbound.jpg", "outbound.jpg"))
			assert(os.path.exists(img2))
			pairs.append((img1, img2))
		elif imgfile.endswith("before.jpg"):
			img1 = imgpath
			img2 = os.path.join(imgdir, imgfile.replace("before.jpg", "later.jpg"))
			assert(os.path.exists(img2))
			pairs.append((img1, img2))
	return pairs

if __name__ == "__main__":
	print get_paired_images(sys.argv[1])