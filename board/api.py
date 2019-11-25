import urllib
import json
from pprint import pprint

class TEST:
    def restapi(self):
        url = "http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc/getNearbyMsrstnList?tmX=244148.546388&tmY=412423.75772&ServiceKey=HSdAuLPQ8rK4KrgTjunCGfbBkLFacZkgmIqaFc4a9FnQUM5rBo0n2tmP%2BNu1DxCtAwSJ3BpvybDFgyz9r2A9pg%3D%3D"
        serviceKey = "HSdAuLPQ8rK4KrgTjunCGfbBkLFacZkgmIqaFc4a9FnQUM5rBo0n2tmP%2BNu1DxCtAwSJ3BpvybDFgyz9r2A9pg%3D%3D"
        #url = "http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc"
        #url = "http://openapi.jejutour.go.kr:8080/openapi/service/TourSpotInfoService/getTourSpotRelate?serviceKey=" + ServiceKey + "&SEQ=310&numOfRows=100&_type=json"
        #url = "http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc/getMsrstnList?addr=서울&stationName=종로구&pageNo=1&numOfRows=10&ServiceKey=HSdAuLPQ8rK4KrgTjunCGfbBkLFacZkgmIqaFc4a9FnQUM5rBo0n2tmP%2BNu1DxCtAwSJ3BpvybDFgyz9r2A9pg%3D%3D&_returnType=json"
        url = url + serviceKey
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            print(response_body.decode('utf-8'))
            dict = json.loads(response_body.decode('utf-8'))
            pprint(dict)
        else:
            print("Error Code:" + rescode)
    
