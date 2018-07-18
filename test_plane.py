import requests
from bs4 import BeautifulSoup
import lxml
import html5lib

re=requests.Session()
header={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':'254',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'country=%E5%8F%B0%E7%81%A3; ASP.NET_SessionId=amvbk0p3fxtrfxtrwy3t4b4j; bm_mi=9DC34FF313B7D08FA0D7443322353C4C~p80XFkhliBLuRYOjU7sJ9CIih2sIdDy6jREp7Ol+OwQITqSsc5KVh3CH1l79aaRnz9NwnYgZUiS5Qb0qkI0RtWObhJdQQHOrzQR9P00GEEMcuujdWf/TuoH/bDxPUDCL5Oasl4nqvLp9nLtmhEAP/l7ZXU3IYXimWF7q5o3b/h5kD6wkEW8hNF70ipKy1y8z3EmQJQevwWx9Rt3O+jJoO8C8jN5FSXvSqGArpcmwgSC0wBAGJ45m5KeRUlo0e2fz8cEpMnLnl8l2pDu87SqGvwCCw/mMS964M5lAlE8C2hipTjKvPz1DEFFrE1MSi0Jk3g4MuH2s5MjxCOj+kMYTxQ==; dtPC=-; dtCookie=2AB6DD4FCDC63B33AB245CE0689ADF5D|T0xCTnwx; _ga=GA1.3.447367103.1500963900; _gid=GA1.3.1677746812.1500963900; bm_sv=21140F3E6FFD6FADAA1C0A9F6D403B23~hFrQuRGXRlYW8NuRctpBlyv6EiB3bFk7lDxOyTYBSxilgEnGNjpRco25BXXoEwKZ7Zz24zVPBJk2deLYj0yCMpWmMn/yFWQmz0dl8YOxo4HxOo5RvHwhwqi/zlIrPslazJXJgUzphaRhnl64DkqqFiVrK2VGw44RBCNm8ldB8os=; ak_bmsc=B06CA9891F0CED93A2EFB7A1312813BFCB458AC0673700006AE476590E2F4D76~plh+61HWIwXAdSIBqO7o7CMlSmbONaKHi6yQhwv1zAxpYEbB8U3QaROQHYisLEs6UaTBpIZ4STI3V0MJW22/gVTu3w3/Aq7MVIZulxi0Yb56YRMRR/OdtuF0CnlhUu3eXDbUldCi5Nn+JvvmWUebOhKXQRFXEdWqwekJwHjxL08ymRfhB9vk1zkdbzFMjvat7HhFhFT8lUxLfT/whpi1xDTZB/uCTxm7tKlraPIuN0x/mJt0cB2RTPVvlIijzXIsb/; dtLatC=48; __utmt_track0=1; __utmt_track1=1; __utmt_UA-46599335-8=1; _dc_gtm_UA-63072599-7=1; _gat_UA-46599335-1=1; _gat_UA-54880298-3=1; _dc_gtm_UA-34980571-20=1; __utma=225761605.447367103.1500963900.1500963900.1500963900.1; __utmb=225761605.7.10.1500963900; __utmc=225761605; __utmz=225761605.1500963900.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _ga=GA1.2.447367103.1500963900; _gid=GA1.2.1677746812.1500963900; _gat_UA-34980571-20=1; flightSearchResult=1; flightSearchResultFrom=%E5%8F%B0%E5%8C%97(%E6%A1%83%E5%9C%92)-TPE-%E5%8F%B0%E7%81%A3; flightSearchResultTo=%E5%A4%A7%E9%98%AA-KIX-%E6%97%A5%E6%9C%AC; flightSearchResultLang=%2Ftw%2Fzh',
'Host':'bookingportal.china-airlines.com',
'Origin':'https://www.china-airlines.com',
'Referer':'https://www.china-airlines.com/tw/zh',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',}
from_data={'B_DATE_1':'201707250000',
'B_LOCATION_1':'TPE',
'E_LOCATION_1':'KIX',
'EBA':'TW',
'SessionID':'zilaeqvhahita1pexg0taujc',
'STUDENTS':'0',
'ADULTS':'1',
'CHILDS':'0',
'INFANTS':'0',
'LANG':'TW',
'Token':'',
'returnURL':'http://www.china-airlines.com/tw/zh',
'TRIP_TYPE':'O',
'selectedMonth':'',
'CABIN':'Y',
'Channel':'CMS',
}
res1=re.post("https://bookingportal.china-airlines.com/eRetailPortal/Booking.svc/Booking/LateLogin",headers=header,data=from_data)

header1={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':'8145',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'''country=%E5%8F%B0%E7%81%A3; bm_mi=9DC34FF313B7D08FA0D7443322353C4C~p80XFkhliBLuRYOjU7sJ9CIih2sIdDy6jREp7Ol+OwQITqSsc5KVh3CH1l79aaRnz9NwnYgZUiS5Qb0qkI0RtWObhJdQQHOrzQR9P00GEEMcuujdWf/TuoH/bDxPUDCL5Oasl4nqvLp9nLtmhEAP/l7ZXU3IYXimWF7q5o3b/h5kD6wkEW8hNF70ipKy1y8z3EmQJQevwWx9Rt3O+jJoO8C8jN5FSXvSqGArpcmwgSC0wBAGJ45m5KeRUlo0e2fz8cEpMnLnl8l2pDu87SqGvwCCw/mMS964M5lAlE8C2hipTjKvPz1DEFFrE1MSi0Jk3g4MuH2s5MjxCOj+kMYTxQ==; ak_bmsc=B06CA9891F0CED93A2EFB7A1312813BFCB458AC0673700006AE476590E2F4D76~plh+61HWIwXAdSIBqO7o7CMlSmbONaKHi6yQhwv1zAxpYEbB8U3QaROQHYisLEs6UaTBpIZ4STI3V0MJW22/gVTu3w3/Aq7MVIZulxi0Yb56YRMRR/OdtuF0CnlhUu3eXDbUldCi5Nn+JvvmWUebOhKXQRFXEdWqwekJwHjxL08ymRfhB9vk1zkdbzFMjvat7HhFhFT8lUxLfT/whpi1xDTZB/uCTxm7tKlraPIuN0x/mJt0cB2RTPVvlIijzXIsb/; D_SID=1.160.104.35':'jy8Q/eZxH3ulkXB4Ako4kcyx31LC8pf4LRZ7ZeHpzHQ; um_jst=6C84D8385C2A118ECA43A44DF9CE1017621BBF6A56496B40F28A9C798473F689; DWM_XSITECODE=CARMCARM; __utmt_track0=1; __utmt_track1=1; __utmt_UA-46599335-8=1; _dc_gtm_UA-63072599-7=1; _gat_UA-46599335-1=1; _gat_UA-54880298-3=1; _dc_gtm_UA-34980571-20=1; D_IID=C3A18F4A-1B31-3936-88E8-1E7C7119D555; D_UID=37228642-508C-3F7A-B91C-2948900EB994; D_ZID=91A57A43-B671-3BF5-9679-81ED77306837; D_ZUID=DBEA1253-9475-3F95-8A32-DC32DCC51F5B; D_HID=709D897E-4381-3298-9557-DBAE55A25BC3; __utma=225761605.447367103.1500963900.1500963900.1500963900.1; __utmb=225761605.7.10.1500963900; __utmc=225761605; __utmz=225761605.1500963900.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _ga=GA1.2.447367103.1500963900; _gid=GA1.2.1677746812.1500963900; _gat_UA-34980571-20=1; flightSearchResult=1; flightSearchResultFrom=%E5%8F%B0%E5%8C%97(%E6%A1%83%E5%9C%92)-TPE-%E5%8F%B0%E7%81%A3; flightSearchResultTo=%E5%A4%A7%E9%98%AA-KIX-%E6%97%A5%E6%9C%AC; flightSearchResultLang=%2Ftw%2Fzh; bm_sv=21140F3E6FFD6FADAA1C0A9F6D403B23~hFrQuRGXRlYW8NuRctpBlyv6EiB3bFk7lDxOyTYBSxilgEnGNjpRco25BXXoEwKZ7Zz24zVPBJk2deLYj0yCMpWmMn/yFWQmz0dl8YOxo4HxOo5RvHwhwqi/zlIrPslaPGLIhGL6n/f7Dn5K0Dx3TyNztaUBRP6nBGtAF44s0F0=; dtLatC=30; dtCookie=2AB6DD4FCDC63B33AB245CE0689ADF5D|T0xCTnwx; dtPC=364862110_227h2''',
'Host':'book.china-airlines.com',
'Origin':'https://bookingportal.china-airlines.com',
'Referer':'https://bookingportal.china-airlines.com/eRetailPortal/Booking.svc/Booking/LateLogin',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
}
from_data={'EMBEDDED_TRANSACTION':'FlexPricerAvailability',
'ENC':'A995A4486D5869E1CE86EA200FEA58D89955C44A4242403E0E5B1C5DE56163F7B82D01245265CE74A05B338B982130EC7B0419DF9E9D418233B5CCD6DF663FCACA192703A423C1DCD310F5932EA343ED308128C472D4AFF66638092C98EF49E15F1E50FA54071A0F9A97B0316F282CFE01C130310DF358C40D26864314047647791024BD8185EC6A1D66F2F0ECC20C3244B4A56E0ED88E7D1DB205D24AD7E3B295EFC8E770ED95373F90FBE55032FEEE0B1530F4412E15ECBBF286F03AA59F0E9EC613E258B0B94A02B22FE3A4D417837ABE8782E84CA86586E446947E07B853D8858F476CFE57F648B266DCCA2DE03076AF24E74EB658E01F2827DE6C1333493D05306CBBC970CC9545A0FEAD3346640C557C0246472BB45CA61B9EEE2DFB94A7DD3F76B4987EEADC17FCC11D2ECC5A6F992B22F408F3E58D1ACF6C8F8B331B2DDC16D773DAE761B54FF19CC618284E74F897C200464F53F3C40A6F9488AC2262FC697C33BAA5A3B0E4A7C40CBE13FE7D5601A042C02D8C9437936567228057D3DF4750240A90CF69C544D9F46EE03FA49A8F8CFE50C17ED8CFC3281E4D8C674F69FC3FC1A37D4789D81FB1ABDCEDD71689BD30CA2F061D2C5DB7706AE9E175C965DED41F7F4AED2F58C9D8CBA37B9475BB3C6BE3F3DCDF36FE716DAB0057A940802DE4C40548AF65F6AFE39A5C4A586DD628F4B442A843C5FA2D384560FA8048F7797CC1975FD76847E6DA0537FD7289DC043A091729A5051ADEEC74E18142DF6CEDDF7C7EF97DB33269AAA8F18658013CDF12C013EA7030DF00B07AC191611B923E8A3AC74AAD038B2BA6D5A0FB106F748845F4AC53C08334E309DDC5187E662F3D06E5426F36F106E3A0079BAA4BB23AA0C6D977A79820F4C2CD6B1F479C6397B92D72FC1E6756C4F5651D5859162A739B4AC66454DAAFCDBCB9FABA69273260DB3EF44B1C4F556DDA5688584ED0CE72ABDD94D0A2C33BDF4F1A5D8C764A1B3D64FC7DD929BCB6C46ED65EB274F6CD40D937C6F046F8371C64275EC227639CC7EA815DA05C7D31E43A2A19C7CFB9366F870E50EFE9CDB9403A6B9730F7AE72D9DD0D4D458FE1219C17654E78AA9C9BEAEA5C2CAACD44A5EB305137EBC043B7E710B692EFA430B5A85A48E1DA25ADB989954E2E6AC22D36E62B79870D203DD851C437EAC00A5F2ECB56E0DBE167CB1E7B0913E6C0A0D08832BE58AAA3ACED3AF7AD559E606818B26FFB8FFACDC1A2155CF86DA4A2BE6035A04263BE8A9D3987D16B3CF6629C95F8BA5E4A7207260F8D2E62AA731E3C84612371349C1A8D2CFE3C97526389F8E56DB50108ABA3F5813D2C9185D1F057A8349559EAE02188EC49A88EBFB07DCF4986DA5C54B025B02D61FAD8E4C270D35B882B5C998FC794F370DB96CBADA6280E0A85C73033C4A357C33E3B69BD9C16B982787C755401D173B82B03F50163A2F69BD3B87B77918B7900F5E67EBB668FFA97DE402A2CE575615FE9FCF54EB9A692942056E712FCA155F226EE8A2BB7A4E6BB28BB7031E60C0D03C03BB795B5955B8D1828B4650B2FC7C1C564B8C8E2552F0443E36A927FCE964F29983827A1F388CD844A7B8F70FC4828E301106CEF2DCDD8E6882568454EE24F29983827A1F388CD844A7B8F70FC4805D0AEB5504F8AF81C8D9220F6E1FDACE1F07D33F77BC5D8A7CF3A392AA1D1B888AF25C6C0B03D676CBC6B1B0479268AA433E8013D3170D891D59BDCD7F93C8922C94D0B9BED8BA33415DDEF37A6423A0BC0FF908F68AD5F756DD3C87A97007B9EDC5C9AA0585B4D93DF8A40E2BB8362D20528CB73BCBD7B5306BB3643B9AB950DBA9A8522962D0E1F639C235941580EE6C001BF28CB60A843F5343AE8D0368B64D34F1177D379CAF8E433468677322937E39189467463601A83190BAFA14B80991063226D6908F80CFA0DEB146C7D52E5DC10EED1F1D2683CA34AD39FEE7AC072E7974DBCAA8C8893E24D92A74ED5B98BB77299562D67C2101CFCCE319F4EF962DC0EBCD2045BB9FFDF3B75AD270FE68BB77299562D67C2101CFCCE319F4EF95799176072D8CB1C761878DC433B3152059A2F992AF23FC6539D22DE5337F9E5F70FE9716B0235771D981848EE00C68A4F29983827A1F388CD844A7B8F70FC4805D0AEB5504F8AF81C8D9220F6E1FDAC3E89CB9BD3E2B5C6037D25E06336CFD1513750C414F85B878D066E9A4870FA6B52761CBCAD4415E928EDD146A6B296F2696108CCE82269FAE7DCFF441730B087CD4FAE3AC493D120042E14D6976EC8F220FF6425EBE4BC6FEFF86AEB20B1BF7F00695AFEE4E1E1511D48186D6350D355EEB1DF4937EF7989C9B1BAB32C975AC2A5273EB3087E67E6D5D5ED9A667F5F5B4A85B671B49C1E19993BBA91F47731CDD323054551B5B22AB57C3DA88175690847CF78349531ABAEE85508B073B9C9F0D323054551B5B22AB57C3DA881756908FCC1A9D1E7721F7177AF3B433F86E00AB3898C40F8DEC0ACDB6DA84042782982B2AF37F69DF837A6D1E57DE50E287D0BD1B6F1450690BF0D80EBF5BB2E3B48927E759D7837163DC4B87E131652B67A2505D0AEB5504F8AF81C8D9220F6E1FDAC3E89CB9BD3E2B5C6037D25E06336CFD19BD0155900ADDA7F03A18CA7F24DCE3D162D7A81E4DB145A38FD7D9EC6EAE4BD6C8F46D97A5D546E92151D6D3BE798ABB0B8156AA5E0D0F441253DAAF6A4144FD1FD5818A6E3B7FECDEF36665A50673730C1165182E18774BC4D23745F40653A184546AD45BD9457C106443E92935E688A1BA1E54E6CD2D335A716B04D40CC638BB77299562D67C2101CFCCE319F4EF962DC0EBCD2045BB9FFDF3B75AD270FE68BB77299562D67C2101CFCCE319F4EF95799176072D8CB1C761878DC433B3152059A2F992AF23FC6539D22DE5337F9E5F70FE9716B0235771D981848EE00C68A4F29983827A1F388CD844A7B8F70FC4805D0AEB5504F8AF81C8D9220F6E1FDAC3E89CB9BD3E2B5C6037D25E06336CFD1513750C414F85B878D066E9A4870FA6B52761CBCAD4415E928EDD146A6B296F2696108CCE82269FAE7DCFF441730B087CD4FAE3AC493D120042E14D6976EC8F25588F45C06A8014A55BE84F57222FB5E4E9747C89F80DDFC5F09DA12E56BAEA720830A7F7643D9A1559F3593928670368BB77299562D67C2101CFCCE319F4EF962DC0EBCD2045BB9FFDF3B75AD270FE68BB77299562D67C2101CFCCE319F4EF95799176072D8CB1C761878DC433B3152059A2F992AF23FC6539D22DE5337F9E5F70FE9716B0235771D981848EE00C68A4F29983827A1F388CD844A7B8F70FC4805D0AEB5504F8AF81C8D9220F6E1FDAC3E89CB9BD3E2B5C6037D25E06336CFD1513750C414F85B878D066E9A4870FA6B52761CBCAD4415E928EDD146A6B296F24804224D8421BE7BA8A607D2F779FBAEBCE4ABD986D971E2472A79DD02FA749E859B049A1DFFD684A9EA421A1291690D151D7A4AEE0686DC9F07151AE003551A264FB52868A5E87032F0A918016A1491BD6F255171385D9C6AEAC642FDA43780CCC17F8555C6FD35B8334623000DED48A0A7205DF9B1C6F285C8F91DF569AD6F8059A445742CE904A64B3A3D60A2BDD7059A2F992AF23FC6539D22DE5337F9E52FBA4CDF0F971C3A8B4F9E63B084F229059A2F992AF23FC6539D22DE5337F9E525D4B04B375120C1F23E8AF7802A2098059A2F992AF23FC6539D22DE5337F9E598D66DCD4965824C6CF6244ADD42F233059A2F992AF23FC6539D22DE5337F9E530C5A423ADCDEEEBF52497E9B321990C71A26DB0E6CBC0A5139915077AC7EDEAFCC1A9D1E7721F7177AF3B433F86E00A5799176072D8CB1C761878DC433B3152059A2F992AF23FC6539D22DE5337F9E530C5A423ADCDEEEBF52497E9B321990C71A26DB0E6CBC0A5139915077AC7EDEAFCC1A9D1E7721F7177AF3B433F86E00A5799176072D8CB1C761878DC433B3152059A2F992AF23FC6539D22DE5337F9E530C5A423ADCDEEEBF52497E9B321990C71A26DB0E6CBC0A5139915077AC7EDEAFCC1A9D1E7721F7177AF3B433F86E00A5799176072D8CB1C761878DC433B3152059A2F992AF23FC6539D22DE5337F9E530C5A423ADCDEEEBF52497E9B321990C71A26DB0E6CBC0A5139915077AC7EDEAFCC1A9D1E7721F7177AF3B433F86E00AE0BCA8F318C6F1A248EEF13D7556F39E7D6F3956B7A5D908AB2E12ED04EA76B56CBE66CA10175E0D942696942D8B4CDF64D34F1177D379CAF8E43346867732295775C367CE8BF2C92BDE95854C48F3104F29983827A1F388CD844A7B8F70FC48CDC0252C72490232F2FA3632FC52DB6A4F29983827A1F388CD844A7B8F70FC48DE5A4BCCFF7D7A50EB8414CFD29350114F29983827A1F388CD844A7B8F70FC4805D0AEB5504F8AF81C8D9220F6E1FDAC3E89CB9BD3E2B5C6037D25E06336CFD1513750C414F85B878D066E9A4870FA6B3A0C2D3984436C4160E4A0FD4D3594387E759D7837163DC4B87E131652B67A2505D0AEB5504F8AF81C8D9220F6E1FDAC3E89CB9BD3E2B5C6037D25E06336CFD1513750C414F85B878D066E9A4870FA6B3A0C2D3984436C4160E4A0FD4D3594387E759D7837163DC4B87E131652B67A2505D0AEB5504F8AF81C8D9220F6E1FDAC3E89CB9BD3E2B5C6037D25E06336CFD1513750C414F85B878D066E9A4870FA6B3A0C2D3984436C4160E4A0FD4D3594387E759D7837163DC4B87E131652B67A2505D0AEB5504F8AF81C8D9220F6E1FDAC3E89CB9BD3E2B5C6037D25E06336CFD1513750C414F85B878D066E9A4870FA6B52761CBCAD4415E928EDD146A6B296F24804224D8421BE7BA8A607D2F779FBAE1684EBB3D11531067B97789F7C5DA2FD0D1A6338CD19A08C26C85C197E92185F4C052331AE12C27EBA2CDDC7296740351D09113F93366F34A631ABE3A05D1BC286674FAD62EF2C37CDA48A5F3A0568682D521D8A2601E21C3579340A5D5CD7E22403977659BF43D477F5E20BA2CBE7F3B8A3187091FC9D7A3AEC7171B3142171B28FE761053A0C151A68083A0BC680711007A5AFC16DE5092CF8865EB3E3672C03E94FA65598D8C250B3258E3A357B57AD6DED71A0F9E8BF2CE7B8AB88965FDBD4E71C668D26EBF3B94B2E47FCF724E63D5BD719AA06F2BFD78C3B288760E1891B8541E68D687C7D1D1E11FD949AB316DE2F7F9507674A2BD327332FCC9AD2EB7DB6166D55DAF3ADFA9C505C422024E1A329E1693ADA40365170A123B95AE0F0DB357760F0112DD76AB483ED69867BC7C4C1379F20AB25855CCDC1CF0A4A7FEADACCC3D559A1982AB8D70909E927F7720BF3490240634C970F98C79A3FA308D8B54D491BD66D20855A7477DA96D97222BC24883FA6EE3EF458EB54E25F0A3E4456AFA0CF528CFD0FD0E44E23616C32A71868E4494C2EE432E31D5A48CE7246C78B6C09E8DD876B532F7E10199190A80A462581348DA1D5E16FD999396A2FD0FDFAC875B512679E7BE798D7C200119FDC9E29294A7B4103157FBD7676DAF9E2FB3F49AD8B13501A22E60BF94AB06587121F93B08053B5EC39E227FC52D6B32B5EA2BD888856F5CFFF21AB73B2B086D14C21F81D7F204F33B4F5B15263AF0FDCFDE4B5EAEE2A1DA3C0263293164254771849DF74B320763CD8EBF6F32006A74AF1F78D212007D23F96BCAACDF9C6423028',
'ENCT':'1',
'SITE':'CARMCARM',
'LANGUAGE':'TW',
}
# proxies={"https":"https://202.171.151.218:8080"}
res=re.post("https://book.china-airlines.com/plnext/FPChinaAirlines/Override.action",headers=header1,data=from_data)
print(res.text)

