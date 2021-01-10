import time

signal = str(59728839950345262750652573835965979939888018102191625099946787791682326347549309844135638586166731548034760365897189592233753445638181247676324660686068855684292956604998590827637221627543512414238407861211421936232231340691500214827820904991045564597324533808990098343557895760522104140762068572528148690396033860391137697751034053950225418906057288850192115676834742394553585487838826710005579833289943702498162546384263561449255093278108677331969126402467573596116021040898708023407842928838817237736084235431065576909382323833184591099600309974914741618495832080930442596854495321267401706790270027803358798899922938307821234896434934824289476011)
# signal = signal * 10
# signal = str(19617804207202209144916044189917)

start = time.time()

for _ in range(100):
    newsignal = []
    for i, _ in enumerate(signal, 1):
        pattern = [0]*(i) + [1]*i + [0] * i + [-1]*i
        newsignal.append(0)
        for j, s in enumerate(signal, 1):
            newsignal[-1] += int(s)*pattern[j%len(pattern)]
    
    
    for i,s in enumerate(newsignal):
        newsignal[i] = str(abs(s)%10)
        
    signal = ''.join(newsignal)
    
duration = time.time()-start    
correctans = 30369587
initduration = 19.3
print('Correct= {} in {} seconds'.format(signal[:8], duration))
print('Correct= {} in {} seconds'.format(correctans, initduration))
