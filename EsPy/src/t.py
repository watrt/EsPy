main_show=False
ili.textst('指数:%s' % weather['data']['yesterday']['aqi'], 10, 6*13, ili.brg(r=255))
ili.textst('位置KEY:%s' % weather['cityInfo']['citykey'], 10, 7*13, ili.brg(r=255))
ili.textst('更新时间:%s' % weather['cityInfo']['updateTime'], 10, 8*13, ili.brg(r=255))