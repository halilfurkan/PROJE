print ( '**HESAP MAKİNESİNE HOŞGELDİNİZ**' )
print ( """İŞLEMLER
1 = TOPLAMA
2 = ÇIKARMA
3 = ÇARPMA
4 = BÖLME
5 = ÜST ALMA
6 = KAREKÖK
7 = KARESİNİ HESAPLAMA
8 = MUTLAK DEĞER 
9 = FAKTÖRİYEL  
10 = LOGARİTMA 
11 = TRİGONOMETRİ
12 = MOD ALMA 
13 = ÇIKIŞ """ )
yazdır ( "*" * 150 )
yazdır ( "*" * 150 )
 Doğru iken :
    hesaplama  =  girdi ( 'LÜTFEN YAPMAK İSTEDİĞİNİZ İŞLEM NUMARASINI GİRİNİZ :' )

    if  hesaplama  ==  '13' :
        print ( 'HESAP MAKİNESİNDEN ÇIKILIYOR ...' )
        kırmak

    elif  hesaplaması  ==  '1' :
        etkisiz_element  =  0
         Doğru iken :
            eklemek  =  şamandıra ( giriş ( '0, bir Başınız) Için toplamak istediginiz Sayıları giriniz (çıkmak' ))
            eğer  eklenti  ==  0 :
                kırmak
            etkisiz_element  +=  ekle
        yazdırmak ( 'TOPLAMA isleminin Sonucu:' , ineffective_element )

    elif  hesaplaması  ==  '2' :
        boole  =  Doğru
        etkisiz_element  =  0
         Doğru iken :
            çıkarma  =  float ( girdi ( 'ÇIKARMAK İSTEDİĞİN SAYILARI SIRAYLA GİRİNİZ (Çıkmak için 0 a a):' ))
            eğer  çıkarma  ==  0 :
                kırmak
            elif  boole  ==  Doğru :
                etkisiz_element  +=  çıkarma
                boole  =  Yanlış
            başka :
                etkisiz_element  -=  çıkarma
        yazdırmak ( 'çıkarma isleminin Sonucu:' , ineffective_element )

    elif  hesaplaması  ==  '3' :
        etkisiz_element  =  1
         Doğru iken :
            çarpma  =  şamandıra ( giriş ( 'çarpmak İstediğiniz Sayıları giriniz (çıkmak 1 a Başınız) için:' ))
            eğer  çarpma  ==  1 :
                kırmak
            etkisiz_element  *=  çarpma
        yazdırmak ( 'Çarpma isleminin Sonucu:' , ineffective_element )

    elif  hesaplaması  ==  '4' :
        etkisiz_element  =  1
         Doğru iken :
            böl  =  int ( giriş ( '1 Için bölmek İstediğiniz Sayıları Sırayla giriniz (çıkmak bir Başınız)' ))
            eğer  böl  ==  1 :
                kırmak
            etkisiz_element  /=  böl
        yazdırmak ( 'BÖLME isleminin Sonucu:' , ineffective_element )

    elif  hesaplaması  ==  '5' :
        a  =  int ( girdi ( 'TABAN YAZINIZ: ' ))
        b  =  int ( input ( 'ÜST YAZINIZ: ' ))
        eğer  bir  ==  0  ve  b  ==  0 :
            yazdır ( 'BELİRSİZ !!' )
        başka :
            yazdırmak ( '* {} isleminin Sonucu} {: {}' . formatını ( a , b , bir  *  b ))

    elif  hesaplaması  ==  '6' :
        a  =  int ( input ( 'KAREKÖKÜNÜ HESAPLAMAK İSTEDİĞİNİZ SAYIYI GİRİNİZ: ' ) )
        baskı ( '{} SAYISININ KAREKÖKÜ: {}' . biçimini ( bir , bir  **  0.5 ))

    elif  hesaplaması  ==  '7' :
        a  =  int ( input ( 'KARESİNİ HESAPLAMAK İSTEDİĞİNİZ SAYIYI GİRİNİZ: ' ))
        baskı ( '{} SAYISININ Karesi: {}' . biçimini ( bir , bir  **  2 ))

    elif  hesaplaması  ==  '8' :
        a  =  int ( input ( 'İLK SAYIYI GİRİNİZ: ' ))
        b  =  int ( girdi ( 'İKİNCİ SAYIYI GİRİNİZ ' ) )
        c  =  a  +  b
        Eğer  c  <  0 :
            mutlak_değer  =  c  *  - 1
            yazdırmak ( 'MUTLAK DEĞERİN Sonucu:' , absolute_value )
        başka :
            yazdır ( 'MUTLAK DEĞERİN SONUCU:' , c )

    elif  hesaplaması  ==  '9' :
        a  =  int ( input ( 'FAKTÖRİYELİNİ HESAPLAMAK İSTEDİĞİNİZ SAYIYI GİRİNİZ: ' ))
        faktöriyel  =  1
        eğer  bir  <  0 :
            print ( "NEGATİF SAYILARIN FAKTÖRİYELİ HESAPLANAMAZ." )
        başka :
            için  I  içinde  aralığı ( 1 , bir  +  1 ):
                faktöriyel  *=  i
            print ( 'SAYININ FAKTÖRİYELİ:' , faktoriyel )

    elif  hesaplaması  ==  '10' :
        ithalat  matematik
        a  =  int ( input ( "LÜTFEN 0'DAN BÜYÜK BİR SAYI GİRİNİZ:" )
        süre ( Doğru ):
            eğer  bir  <=  0 :
                print ( "LÜTFEN 0'DAN BÜYÜK BİR SAYI GİRİNİZ:" )
                kırmak
            başka :
                yazdır ( matematik . log10 ( a ))
                kırmak
