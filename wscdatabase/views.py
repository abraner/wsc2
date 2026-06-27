from django.shortcuts import render, redirect, get_object_or_404
from .models import ContractorInfo, CustomerInfo, CurrentRm, BidTbl, BidTbl2, TotalRoomCost, Pricing, CompOption, \
    AccOption, Cabinet, Drawer, CabSide, RoomType, WoodSpecies, DoorStyle, FinishColor, FinishOption, Comp, \
    CompOptionTotal, CabAcc, AccOptionTotal, Totals, ConDelete, DeleteRm, DeleteCust, JobCost, ContractOption, TaxRate, \
    Labor, Contract, IncludedOption, IncludedAcc, ContractInclude, ContractIncludeTotal, Percentage, Agreement, \
    WorkType, Ultimate, Include, Exclude, Legally5, Legally1, Legally2, Legally3, Legally4
from django.core.paginator import Paginator
from .forms import Custinfo, Coninfo, DupConInfo, ConinfoA, BidPage, BidPage2, TotalRmCost, CurrRm, \
    AddNewRm, RoomChoiceField, RmSelection, CustinfoB, CustinfoC, JobCostForm, CompLabor, ConTract, BidPageSelection
from django.db.models import Q, Sum, F
from django.http import HttpResponseRedirect
from num2words import num2words
import time



def welcome(request):
    return render(request, 'wsc/welcome.html')


def red(request):
    return render(request, 'wsc/red.html')


def main(request):
    return render(request, 'wsc/main.html')


def addnewrm(request):
    return render(request, 'wsc/addnewrm.html')


def delete(request):
    a = ConDelete.objects.all()
    a.delete()
    return render(request, 'wsc/con_info_existing.html')


def newcon(request):
    if request.method == 'POST':
        form = Coninfo(request.POST)
        if form.is_valid():
            form.save()
            a = ContractorInfo.objects.all()
            d = CustomerInfo.objects.all()
            f = JobCost.objects.all()
            instance2 = ContractorInfo.objects.order_by('id').last()
            b = a.values_list('id', flat=True).last()
            c = CustomerInfo.objects.create(conid=b)
            g = f.create(conid=b)
            h = f.values_list('id', flat=True).last()
            instance6 = CustomerInfo.objects.order_by('id').last()
            e = d.values_list('id', flat=True).last()
            ContractorInfo.objects.filter(id=b).update(idA=b)
            CustomerInfo.objects.filter(id=e).update(custid=e)
            JobCost.objects.filter(id=h).update(jobid=h, custid=e)
            context2 = {
                "instance2": instance2,
                "instance6": instance6,
                "a": a,
                "b": b,
                "c": c,
                "d": d,
                "e": e,
                "g": g,
            }
            ###return render(request, 'wsc/newcon.html', context2)
            return redirect(instance6.get_absolute2_url(), context2)
        else:
            form = Coninfo()
            return render(request, 'wsc/conerror.html', {'form': form})
    else:
        form = Coninfo()
        return render(request, 'wsc/newcon.html', {'form': form})









def deletecon(request, id=None):
    instance = ContractorInfo.objects.get(id=id)
    form = ConinfoA(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    b = AccOptionTotal.objects.all()
    c = BidTbl.objects.all()
    d = BidTbl2.objects.all()
    e = Cabinet.objects.all()
    f = CabSide.objects.all()
    f1 = Contract.objects.all()
    f2 = ContractInclude.objects.all()
    g = CompOption.objects.all()
    h = CompOptionTotal.objects.all()
    i = ContractorInfo.objects.all()
    j = CurrentRm.objects.all()
    k = CustomerInfo.objects.all()
    l = Drawer.objects.all()
    m = TotalRoomCost.objects.all()
    n = Totals.objects.all()
    p = JobCost.objects.all()
    p1 = Labor.objects.all()
    p2 = IncludedOption.objects.all()
    p3 = IncludedAcc.objects.all()
    p4 = ContractIncludeTotal.objects.all()
    a.filter(conid=id).delete()
    b.filter(conid=id).delete()
    c.filter(conid=id).delete()
    d.filter(conid=id).delete()
    e.filter(conid=id).delete()
    f.filter(conid=id).delete()
    f1.filter(conid=id).delete()
    f2.filter(conid=id).delete()
    g.filter(conid=id).delete()
    h.filter(conid=id).delete()
    j.filter(conid=id).delete()
    k.filter(conid=id).delete()
    l.filter(conid=id).delete()
    m.filter(conid=id).delete()
    n.filter(conid=id).delete()
    p.filter(conid=id).delete()
    p1.filter(conid=id).delete()
    p2.filter(conid=id).delete()
    p3.filter(conid=id).delete()
    p4.filter(conid=id).delete()
    i.filter(id=id).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute37_url(), context)


def dupconinfo(request, id=None):
    instance = CustomerInfo.objects.filter(id=id).last()
    form = DupConInfo(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute6_url(), context2)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/dupconinfo.html', context)


def deletecontractor(request, id=None):
    instance = ContractorInfo.objects.get(id=id)
    form = ConinfoA(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute37_url(), context2)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/deletecontractor.html', context)


def yesdupcon(request, id=None):
    instance = get_object_or_404(CustomerInfo, id=id)
    form = DupConInfo(request.POST or None, instance=instance)
    a = ContractorInfo.objects.all()
    b = CustomerInfo.objects.order_by('conid').last()
    c = CustomerInfo.objects.values_list('conid', flat=True).last()
    d = a.values_list('concompanytname', flat=True).get(id=c)
    e = a.values_list('confirstname', flat=True).get(id=c)
    f = a.values_list('conlastname', flat=True).get(id=c)
    g = a.values_list('conadd1', flat=True).get(id=c)
    h = a.values_list('conadd2', flat=True).get(id=c)
    i = a.values_list('concity', flat=True).get(id=c)
    j = a.values_list('const', flat=True).get(id=c)
    k = a.values_list('conzipcode', flat=True).get(id=c)
    l = a.values_list('conwork1', flat=True).get(id=c)
    m = a.values_list('conwork2', flat=True).get(id=c)
    n = a.values_list('concell1', flat=True).get(id=c)
    o = a.values_list('concell2', flat=True).get(id=c)
    p = a.values_list('conhome', flat=True).get(id=c)
    q = a.values_list('conemail1', flat=True).get(id=c)
    r = a.values_list('conemail2', flat=True).get(id=c)
    t = CustomerInfo.objects.all()
    s = CustomerInfo.objects.filter(conid=c).update(custcompanytname=d, custfirstname=e, custlastname=f, custadd1=g,
                                                    custadd2=h, custcity=i, custst=j, custzipcode=k, custwork1=l,
                                                    custwork2=m, custcell1=n, custcell2=o, custhome=p, custemail1=q,
                                                    custemail2=r)

    u = BidTbl.objects.all()
    aaa = BidTbl2.objects.all()
    dd = TotalRoomCost.objects.all()
    jj = CurrentRm.objects.all()
    kk = JobCost.objects.all()
    v = BidTbl.objects.create(conid=c)
    bb = BidTbl2.objects.create(conid=c)
    ee = TotalRoomCost.objects.create(conid=c)
    gg = CurrentRm.objects.create(conid=c)
    instance2 = BidTbl.objects.order_by('id').last()
    instance6 = BidTbl2.objects.order_by('id').last()

    x = u.values_list('id', flat=True).last()
    cc = aaa.values_list('id', flat=True).last()
    ff = dd.values_list('id', flat=True).last()
    hh = jj.values_list('id', flat=True).last()
    z = CustomerInfo.objects.order_by('id').last()
    aa = CustomerInfo.objects.values_list('id', flat=True).last()
    s1 = Contract.objects.create(custid=aa, conid=c)
    BidTbl.objects.filter(id=x).update(bid_idA=x, custid=aa, custlastname=f, custadd1=g, pageid=1, max=1, maxnum=1,
                                       c11qty_id='')

    BidTbl2.objects.filter(id=cc).update(idA=cc, bid_idA=x, custid=aa, pageid=1)
    TotalRoomCost.objects.filter(id=ff).update(bid_idA=x, custid=aa, custlastname=f, custadd1=g)
    CurrentRm.objects.filter(id=hh).update(rm_idA=hh, bid_idA=x, custid=aa)
    Totals.objects.create(bid_idA=x, custid=aa, conid=c)
    JobCost.objects.filter(custid=aa, conid=c).update(custlastname=f, custadd1=g, installtext_id=2, install='No')

    context = {
        "b": b,
        "s": s,
        "t": t,
        'v': v,
        'bb': bb,
        'cc': cc,
        "ee": ee,
        "gg": gg,
        "kk": kk,
        'z': z,
        "s1": s1,
        "instance": instance,
        "instance6": instance6,
        "form": form,
    }
    return redirect(instance2.get_absolute11_url(), context)


def addnewrm2(request, id=None):
    instance = get_object_or_404(CustomerInfo, id=id)
    form = Custinfo(request.POST or None, instance=instance)
    a = ContractorInfo.objects.all()
    c = CustomerInfo.objects.values_list('conid', flat=True).get(id=id)
    f = a.values_list('conlastname', flat=True).get(id=c)
    g = a.values_list('conadd1', flat=True).get(id=c)

    u = BidTbl.objects.all()
    aaa = BidTbl2.objects.all()
    dd = TotalRoomCost.objects.all()
    jj = CurrentRm.objects.all()
    ll = AccOption.objects.all()
    v = BidTbl.objects.create(conid=c)
    bb = BidTbl2.objects.create(conid=c)
    ee = TotalRoomCost.objects.create(conid=c)
    gg = CurrentRm.objects.create(conid=c)
    kk = AccOption.objects.create(conid=c)
    instance2 = BidTbl.objects.order_by('id').last()
    instance6 = BidTbl2.objects.order_by('id').last()

    x = u.values_list('id', flat=True).last()
    cc = aaa.values_list('id', flat=True).last()
    ff = dd.values_list('id', flat=True).last()
    hh = jj.values_list('id', flat=True).last()
    mm = ll.values_list('id', flat=True).last()
    z = CustomerInfo.objects.order_by('id').last()
    aa = CustomerInfo.objects.values_list('id', flat=True).get(id=id)
    BidTbl.objects.filter(id=x).update(bid_idA=x, custid=aa, custlastname=f, custadd1=g, pageid=1, max=1, maxnum=1,
                                       c11qty_id='', rmactive=1)
    BidTbl2.objects.filter(id=cc).update(idA=x, bid_idA=x, custid=aa, pageid=1)
    TotalRoomCost.objects.filter(id=ff).update(bid_idA=x, custid=aa, custlastname=f, custadd1=g)
    CurrentRm.objects.filter(id=hh).update(rm_idA=hh, bid_idA=x, custid=aa)
   ### AccOption.objects.filter(id=mm).update(bid_idA=x, custid=aa, ident=0, accqty=0, acc=0, price=0)
    Totals.objects.create(bid_idA=x, custid=aa, conid=c)
    context = {
        'v': v,
        'bb': bb,
        'cc': cc,
        "ee": ee,
        "gg": gg,
        "kk": kk,
        'z': z,
        "instance": instance,
        "instance6": instance6,
        "form": form,
    }
    return redirect(instance2.get_absolute11_url(), context)


def conerror(request):
    return render(request, 'wsc/conerror.html')


def custerror(request):
    return render(request, 'wsc/custerror.html')


def deletecustconfirm(request, id=None):
    instance = CustomerInfo.objects.get(id=id)
    form = Custinfo(request.POST or None, instance=instance)
    DeleteCust.objects.all().delete()
    a = CustomerInfo.objects.all()
    b = CustomerInfo.objects.values_list('conid', flat=True).get(custid=id)
    c = DeleteCust.objects.create(deletecust=id, deletecon=b)
    instance6 = a.order_by('id').last()
    context2 = {
        "instance6": instance6,
        "form": form,
        "c": c,
    }
    return redirect(instance6.get_absolute45_url(), context2)


def deletecust2(request, id=None):
    instance = CustomerInfo.objects.get(id=id)
    form = Custinfo(request.POST or None, instance=instance)

    a = CustomerInfo.objects.all()
    b = CustomerInfo.objects.values_list('conid', flat=True).get(custid=id)
    c = a.values_list('conid', flat=True).last()
    d = DeleteCust.objects.filter(id=c).update(deletecust=id, deletecon=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute28_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "d": d,
    }
    return render(request, 'wsc/deletecust2.html', context)


def deletecust3(request, id=None):
    instance = CustomerInfo.objects.get(id=id)
    form = Custinfo(request.POST or None, instance=instance)
    b = DeleteCust.objects.values_list('deletecust', flat=True).last()
    c = DeleteCust.objects.values_list('deletecon', flat=True).last()
    d = CustomerInfo.objects.filter(custid=b, conid=c).delete()
    context = {
        "instance": instance,
        "form": form,
        "d": d,
    }
    return redirect(instance.get_absolute28_url(), context)


def newcust(request, id=None):
    if request.method == 'POST':
        instance = CustomerInfo.objects.filter(id=id).last()
        form = CustinfoB(request.POST or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            a = CustomerInfo.objects.all()
            b = BidTbl.objects.all()
            c = BidTbl2.objects.all()
            d = TotalRoomCost.objects.all()
            e = CurrentRm.objects.all()
            oo = Totals.objects.all()
            f = a.values_list('id', flat=True).last()
            ff = a.values_list('conid', flat=True).last()
            gg = a.values_list('custlastname', flat=True).last()
            ee = a.values_list('custadd1', flat=True).last()
            k = BidTbl.objects.create(custid=f, conid=ff, custlastname=gg, custadd1=ee, pageid=1, max=1, maxnum=1,
                                      rmactive=1)
            t1 = b.values_list('id', flat=True).last()
            l = BidTbl2.objects.create(custid=f, conid=ff, pageid=1, idA=t1)
            m = TotalRoomCost.objects.create(custid=f, conid=ff, custlastname=gg, custadd1=ee)
            n = CurrentRm.objects.create(custid=f, conid=ff)
            o = Totals.objects.create(custid=f, conid=ff)
            g = b.values_list('id', flat=True).last()
            h = d.values_list('id', flat=True).last()
            i = e.values_list('id', flat=True).last()
            j = c.values_list('id', flat=True).last()
            jj = oo.values_list('id', flat=True).last()
            instance2 = BidTbl.objects.order_by('id').last()
            instance6 = BidTbl2.objects.order_by('id').last()
            BidTbl.objects.filter(id=g).update(bid_idA=g)
            BidTbl2.objects.filter(id=j).update(bid_idA=g)
            TotalRoomCost.objects.filter(id=h).update(bid_idA=g)
            CurrentRm.objects.filter(id=i).update(rm_idA=i, bid_idA=g)
            Totals.objects.filter(id=jj).update(bid_idA=g)
            JobCost.objects.filter(custid=f, conid=ff).update(custlastname=gg, custadd1=ee, installtext_id=2,
                                                              install='No')
#            s1 = Contract.objects.create(custid=f, conid=ff)
            context = {
                "c": c,
                "k": k,
                "l": l,
                "m": m,
                "n": n,
#                "s1": s1,
                "o": o,
                "instance2": instance2,
                "instance": instance,
                "instance6": instance6,
                "form": form,
            }
            return redirect(instance2.get_absolute11_url(), context)
        else:
            instance = CustomerInfo.objects.filter(id=id).last()
            form = Custinfo(request.POST or None, instance=instance)
            return render(request, 'wsc/custerror.html', {'form': form})

    else:
        instance = CustomerInfo.objects.filter(id=id).last()
        form = Custinfo(request.POST or None, instance=instance)
        return render(request, 'wsc/newcust.html', {'form': form})



def cust_info_existing(request):
    queryset = CustomerInfo.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(custcompanytname__icontains=search_term)
                                   | Q(custfirstname__icontains=search_term)
                                   | Q(custlastname__icontains=search_term)
                                   | Q(custadd1__icontains=search_term)
                                   | Q(custadd2__icontains=search_term)
                                   | Q(custcity__icontains=search_term)
                                   | Q(custst__icontains=search_term)
                                   | Q(custzipcode__icontains=search_term)
                                   | Q(custwork1__icontains=search_term)
                                   | Q(custwork2__icontains=search_term)
                                   | Q(custcell1__icontains=search_term)
                                   | Q(custcell2__icontains=search_term)
                                   | Q(custhome__icontains=search_term)
                                   | Q(custemail1__icontains=search_term)
                                   | Q(custemail2__icontains=search_term))
    paginator = Paginator(queryset, 13)  # Show 6 contacts per page
    page = request.GET.get('page')
    queryset = paginator.get_page(page)
    context = {"object_list": queryset, "search_term": search_term}
    return render(request, 'wsc/cust_info_existing.html', context)


def currentrm(request):
    queryset = CurrentRm.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(bid_idA__icontains=search_term)
                                   | Q(rmnum_id__icontains=search_term)
                                   | Q(rmcost__icontains=search_term)
                                   | Q(rmactive__icontains=search_term)
                                   | Q(rmdelete__icontains=search_term)
                                   | Q(custadd2__icontains=search_term))

    paginator = Paginator(queryset, 13)  # Show 6 contacts per page
    page = request.GET.get('page')
    queryset = paginator.get_page(page)
    context = {"object_list": queryset, "search_term": search_term}
    return render(request, 'wsc/currentrm.html', context)


def con_info_existing(request):
    queryset = ContractorInfo.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(concompanytname__icontains=search_term)
                                   | Q(confirstname__icontains=search_term)
                                   | Q(conlastname__icontains=search_term)
                                   | Q(conadd1__icontains=search_term)
                                   | Q(conadd2__icontains=search_term)
                                   | Q(concity__icontains=search_term)
                                   | Q(const__icontains=search_term)
                                   | Q(conzipcode__icontains=search_term)
                                   | Q(conwork1__icontains=search_term)
                                   | Q(conwork2__icontains=search_term)
                                   | Q(concell1__icontains=search_term)
                                   | Q(concell2__icontains=search_term)
                                   | Q(conhome__icontains=search_term)
                                   | Q(conemail1__icontains=search_term)
                                   | Q(conemail2__icontains=search_term))

    paginator = Paginator(queryset, 13)  # Show 13 contacts per page
    page = request.GET.get('page')
    queryset = paginator.get_page(page)
    context = {"object_list": queryset, "search_term": search_term}
    return render(request, 'wsc/con_info_existing.html', context)


def coninfo(request, id):
    instance = ContractorInfo.objects.get(id=id)
    form = ConinfoA(request.POST or None, instance=instance)
    a = CustomerInfo.objects.all()
    queryset = CustomerInfo.objects.filter(conid=id).values()
    context = {
        "instance": instance,
        "form": form,
        "object_list": queryset,

        "a": a,
    }
    return render(request, 'wsc/coninfo.html', context)


def custinfo(request, id):
    instance = CustomerInfo.objects.get(id=id)
    form = CustinfoB(request.POST or None, instance=instance)
    a = CurrentRm.objects.filter(custid=id).annotate(bid=F('bid_idA'))
    b = list(a.values_list('bid_idA', flat=True))
    try:
        room1 = CurrentRm.objects.filter(custid=id, bid_idA=b[0])
    except Exception:
        room1 = CurrentRm.objects.filter(custid=id, bid_idA=0)
    try:
        room2 = CurrentRm.objects.filter(custid=id, bid_idA=b[1])
    except Exception:
        room2 = CurrentRm.objects.filter(custid=id, bid_idA=0)
    try:
        room3 = CurrentRm.objects.filter(custid=id, bid_idA=b[2])
    except Exception:
        room3 = CurrentRm.objects.filter(custid=id, bid_idA=0)
    try:
        room4 = CurrentRm.objects.filter(custid=id, bid_idA=b[3])
    except Exception:
        room4 = CurrentRm.objects.filter(custid=id, bid_idA=0)
    try:
        room5 = CurrentRm.objects.filter(custid=id, bid_idA=b[4])
    except Exception:
        room5 = CurrentRm.objects.filter(custid=id, bid_idA=0)
    try:
        room6 = CurrentRm.objects.filter(custid=id, bid_idA=b[5])
    except Exception:
        room6 = CurrentRm.objects.filter(custid=id, bid_idA=0)
    try:
        room7 = CurrentRm.objects.filter(custid=id, bid_idA=b[6])
    except Exception:
        room7 = CurrentRm.objects.filter(custid=id, bid_idA=0)
    try:
        room8 = CurrentRm.objects.filter(custid=id, bid_idA=b[7])
    except Exception:
        room8 = CurrentRm.objects.filter(custid=id, bid_idA=0)
    try:
        room9 = CurrentRm.objects.filter(custid=id, bid_idA=b[8])
    except Exception:
        room9 = CurrentRm.objects.filter(custid=id, bid_idA=0)
    try:
        room10 = CurrentRm.objects.filter(custid=id, bid_idA=b[9])
    except Exception:
        room10 = CurrentRm.objects.filter(custid=id, bid_idA=0)
    try:
        room11 = CurrentRm.objects.filter(custid=id, bid_idA=b[10])
    except Exception:
        room11 = CurrentRm.objects.filter(custid=id, bid_idA=0)
    try:
        room12 = CurrentRm.objects.filter(custid=id, bid_idA=b[11])
    except Exception:
        room12 = CurrentRm.objects.filter(custid=id, bid_idA=0)
    try:
        room13 = CurrentRm.objects.filter(custid=id, bid_idA=b[12])
    except Exception:
        room13 = CurrentRm.objects.filter(custid=id, bid_idA=0)

    context = {
        "instance": instance,
        "form": form,
        "room1": room1,
        "room2": room2,
        "room3": room3,
        "room4": room4,
        "room5": room5,
        "room6": room6,
        "room7": room7,
        "room8": room8,
        "room9": room9,
        "room10": room10,
        "room11": room11,
        "room12": room12,
        "room13": room13,
    }
    return render(request, 'wsc/custinfo.html', context)

def custinfo1(request, id):
    instance = CustomerInfo.objects.get(id=id)
    form = CustinfoB(request.POST or None, instance=instance)
    queryset = CurrentRm.objects.filter(custid=id)
    context = {
        "instance": instance,
        "form": form,
        "object_list": queryset,
    }
    return render(request, 'wsc/room_cost.html', context)


def custinfo2(request, id):
    instance = CustomerInfo.objects.get(id=id)
    form = Custinfo(request.POST or None, instance=instance)
    queryset = CurrentRm.objects.filter(custid=id)
    context = {
        "instance": instance,
        "form": form,
        "object_list": queryset,
    }
    return render(request, 'wsc/custinfo2.html', context)


def deletecust(request, id=None):
    instance = CustomerInfo.objects.get(id=id)
    form = CustinfoB(request.POST or None, instance=instance)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/deletecust.html', context)



def deletecust4(request, id=None):
    instance = CustomerInfo.objects.get(id=id)
    form = Custinfo(request.POST or None, instance=instance)
    a = CurrentRm.objects.all()
    b = BidTbl.objects.all()
    c = BidTbl2.objects.all()
    d = AccOption.objects.all()
    e = AccOptionTotal.objects.all()
    f = CompOption.objects.all()
    g = CompOptionTotal.objects.all()
    h = TotalRoomCost.objects.all()
    i = CustomerInfo.objects.all()
    j = Contract.objects.all()
    j2 = ContractInclude.objects.all()
    k = IncludedOption.objects.all()
    l = IncludedAcc.objects.all()
    t1 = ContractIncludeTotal.objects.all()
    t2 = Cabinet.objects.all()
    p = JobCost.objects.all()
    p1 = Labor.objects.all()
    n = Totals.objects.all()

    a.filter(custid=id).delete()
    b.filter(custid=id).delete()
    c.filter(custid=id).delete()
    d.filter(custid=id).delete()
    e.filter(custid=id).delete()
    f.filter(custid=id).delete()
    g.filter(custid=id).delete()
    h.filter(custid=id).delete()
    i.filter(id=id).delete()
    j.filter(custid=id).delete()
    j2.filter(custid=id).delete()
    k.filter(custid=id).delete()
    l.filter(custid=id).delete()
    t1.filter(custid=id).delete()
    t2.filter(custid=id).delete()
    p.filter(custid=id).delete()
    p1.filter(custid=id).delete()
    n.filter(custid=id).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def prodqueue(request, id=None):
    instance = get_object_or_404(CustomerInfo, id=id)
    form = CustinfoB(request.POST or None, instance=instance)
    d = request.POST['id_prodqueue']
    CustomerInfo.objects.filter(id=id).update(prodqueue_id=d)
    Totals.objects.filter(custid=id).update(increase=d)
    m = Totals.objects.filter(custid=id).annotate(bid=F('bid_idA'), sub_total=F('baseprice') * F('increase'))
    n = Totals.objects.filter(custid=id).annotate(bid=F('bid_idA'), total=F('baseprice') + F('totalincrease'))
    for m in m:
        Totals.objects.filter(bid_idA=m.bid).update(totalincrease=m.sub_total)
        TotalRoomCost.objects.filter(bid_idA=m.bid).update(prodqueuetotal=m.sub_total)
    for n in n:
        Totals.objects.filter(bid_idA=n.bid).update(totalrmcost=n.total)
        CurrentRm.objects.filter(bid_idA=n.bid).update(rmcost=n.total)
        TotalRoomCost.objects.filter(bid_idA=n.bid).update(rmgrandtotal=n.total)
    t1 = Totals.objects.filter(custid=id).annotate(bid=F('bid_idA'), optionsub_total=F('optionnum') * F('increase'))
    t2 = Totals.objects.filter(custid=id).annotate(bid=F('bid_idA'), optiontotal=F('optionnum') + F('optionnumincrease'))
    for t1 in t1:
        Totals.objects.filter(bid_idA=t1.bid).update(optionnumincrease=t1.optionsub_total)
    for t2 in t2:
        Totals.objects.filter(bid_idA=t2.bid).update(optionnumtotal=t2.optiontotal)
        TotalRoomCost.objects.filter(bid_idA=t2.bid).update(optionnum=t2.optiontotal)
    t1a = Totals.objects.filter(custid=id).annotate(bid=F('bid_idA'), accsub_total=F('cabaccrmtotal') * F('increase'))
    t2a = Totals.objects.filter(custid=id).annotate(bid=F('bid_idA'), acctotal=F('cabaccrmtotal') + F('cabaccrmtotalincrease'))
    for t1a in t1a:
        Totals.objects.filter(bid_idA=t1a.bid).update(cabaccrmtotalincrease=t1a.accsub_total)
    for t2a in t2a:
        Totals.objects.filter(bid_idA=t2a.bid).update(cabaccrmtotaltotal=t2a.acctotal)
        TotalRoomCost.objects.filter(bid_idA=t2a.bid).update(cabaccrmtotal=t2a.acctotal)
    gg = CustomerInfo.objects.values_list('prodqueue_id', flat=True).get(custid=id)
    j2 = Pricing.objects.values_list('drawer', flat=True).last()
    o6 = j2 * gg
    p6 = j2 + o6
    TotalRoomCost.objects.filter(bid_idA=n.bid).update(drawercost=p6)

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/room_cost.html', context)


def load_rmcost1(request, id=None):
    instance = CurrentRm.objects.filter(id=id).first()
    form = CurrRm(request.POST or None, instance=instance)
    a = CurrentRm.objects.filter(custid=id).annotate(bid=F('bid_idA'))
    b = list(a.values_list('bid_idA', flat=True))
    try:
        rmcost1 = CurrentRm.objects.values('rmcost').get(custid=id, bid_idA=b[0])
    except IndexError:
        rmcost1 = 0
    context = {
        "instance": instance,
        "form": form,
        "rmcost1": rmcost1,
    }
    return render(request, 'wsc/room_cost.html', context)


def load_rmcost2(request, id=None):
    instance = CurrentRm.objects.filter(id=id).first()
    form = CurrRm(request.POST or None, instance=instance)
    a = CurrentRm.objects.filter(custid=id).annotate(bid=F('bid_idA'))
    b = list(a.values_list('bid_idA', flat=True))
    try:
        rmcost2 = CurrentRm.objects.values('rmcost').get(custid=id, bid_idA=b[1])
    except IndexError:
        rmcost2 = 0
    context = {
        "instance": instance,
        "form": form,
        "rmcost2": rmcost2,
    }
    return render(request, 'wsc/room_cost2.html', context)


def load_rmcost3(request, id=None):
    instance = CurrentRm.objects.filter(id=id).first()
    form = CurrRm(request.POST or None, instance=instance)
    a = CurrentRm.objects.filter(custid=id).annotate(bid=F('bid_idA'))
    b = list(a.values_list('bid_idA', flat=True))
    try:
        rmcost3 = CurrentRm.objects.values('rmcost').get(custid=id, bid_idA=b[2])
    except IndexError:
        rmcost3 = 0
    context = {
        "instance": instance,
        "form": form,
        "rmcost3": rmcost3,
    }
    return render(request, 'wsc/room_cost3.html', context)


def load_rmcost4(request, id=None):
    instance = CurrentRm.objects.filter(id=id).first()
    form = CurrRm(request.POST or None, instance=instance)
    a = CurrentRm.objects.filter(custid=id).annotate(bid=F('bid_idA'))
    b = list(a.values_list('bid_idA', flat=True))
    try:
        rmcost4 = CurrentRm.objects.values('rmcost').get(custid=id, bid_idA=b[3])
    except IndexError:
        rmcost4 = 0
    context = {
        "instance": instance,
        "form": form,
        "rmcost4": rmcost4,
    }
    return render(request, 'wsc/room_cost4.html', context)


def load_rmcost5(request, id=None):
    instance = CurrentRm.objects.filter(id=id).first()
    form = CurrRm(request.POST or None, instance=instance)
    a = CurrentRm.objects.filter(custid=id).annotate(bid=F('bid_idA'))
    b = list(a.values_list('bid_idA', flat=True))
    try:
        rmcost5 = CurrentRm.objects.values('rmcost').get(custid=id, bid_idA=b[4])
    except IndexError:
        rmcost5 = 0
    context = {
        "instance": instance,
        "form": form,
        "rmcost5": rmcost5,
    }
    return render(request, 'wsc/room_cost5.html', context)


def load_rmcost6(request, id=None):
    instance = CurrentRm.objects.filter(id=id).first()
    form = CurrRm(request.POST or None, instance=instance)
    a = CurrentRm.objects.filter(custid=id).annotate(bid=F('bid_idA'))
    b = list(a.values_list('bid_idA', flat=True))
    try:
        rmcost6 = CurrentRm.objects.values('rmcost').get(custid=id, bid_idA=b[5])
    except IndexError:
        rmcost6 = 0
    context = {
        "instance": instance,
        "form": form,
        "rmcost6": rmcost6,
    }
    return render(request, 'wsc/room_cost6.html', context)


def load_rmcost7(request, id=None):
    instance = CurrentRm.objects.filter(id=id).first()
    form = CurrRm(request.POST or None, instance=instance)
    a = CurrentRm.objects.filter(custid=id).annotate(bid=F('bid_idA'))
    b = list(a.values_list('bid_idA', flat=True))
    try:
        rmcost7 = CurrentRm.objects.values('rmcost').get(custid=id, bid_idA=b[6])
    except IndexError:
        rmcost7 = 0

    context = {
        "instance": instance,
        "form": form,
        "rmcost7": rmcost7,
    }
    return render(request, 'wsc/room_cost7.html', context)


def load_rmcost8(request, id=None):
    instance = CurrentRm.objects.filter(id=id).first()
    form = CurrRm(request.POST or None, instance=instance)
    a = CurrentRm.objects.filter(custid=id).annotate(bid=F('bid_idA'))
    b = list(a.values_list('bid_idA', flat=True))
    try:
        rmcost8 = CurrentRm.objects.values('rmcost').get(custid=id, bid_idA=b[7])
    except IndexError:
        rmcost8 = 0
    context = {
        "instance": instance,
        "form": form,
        "rmcost8": rmcost8,
    }
    return render(request, 'wsc/room_cost8.html', context)


def load_rmcost9(request, id=None):
    instance = CurrentRm.objects.filter(id=id).first()
    form = CurrRm(request.POST or None, instance=instance)
    a = CurrentRm.objects.filter(custid=id).annotate(bid=F('bid_idA'))
    b = list(a.values_list('bid_idA', flat=True))
    try:
        rmcost9 = CurrentRm.objects.values('rmcost').get(custid=id, bid_idA=b[8])
    except IndexError:
        rmcost9 = 0
    context = {
        "instance": instance,
        "form": form,
        "rmcost9": rmcost9,
    }
    return render(request, 'wsc/room_cost9.html', context)


def load_rmcost10(request, id=None):
    instance = CurrentRm.objects.filter(id=id).first()
    form = CurrRm(request.POST or None, instance=instance)
    a = CurrentRm.objects.filter(custid=id).annotate(bid=F('bid_idA'))
    b = list(a.values_list('bid_idA', flat=True))
    try:
        rmcost10 = CurrentRm.objects.values('rmcost').get(custid=id, bid_idA=b[9])
    except IndexError:
        rmcost10 = 0
    context = {
        "instance": instance,
        "form": form,
        "rmcost10": rmcost10,
    }
    return render(request, 'wsc/room_cost10.html', context)


def load_rmcost11(request, id=None):
    instance = CurrentRm.objects.filter(id=id).first()
    form = CurrRm(request.POST or None, instance=instance)
    a = CurrentRm.objects.filter(custid=id).annotate(bid=F('bid_idA'))
    b = list(a.values_list('bid_idA', flat=True))
    try:
        rmcost11 = CurrentRm.objects.values('rmcost').get(custid=id, bid_idA=b[10])
    except IndexError:
        rmcost11 = 0
    context = {
        "instance": instance,
        "form": form,
        "rmcost11": rmcost11,
    }
    return render(request, 'wsc/room_cost11.html', context)


def load_rmcost12(request, id=None):
    instance = CurrentRm.objects.filter(id=id).first()
    form = CurrRm(request.POST or None, instance=instance)
    a = CurrentRm.objects.filter(custid=id).annotate(bid=F('bid_idA'))
    b = list(a.values_list('bid_idA', flat=True))
    try:
        rmcost12 = CurrentRm.objects.values('rmcost').get(custid=id, bid_idA=b[11])
    except IndexError:
        rmcost12 = 0
    context = {
        "instance": instance,
        "form": form,
        "rmcost12": rmcost12,
    }
    return render(request, 'wsc/room_cost12.html', context)


def load_rmcost13(request, id=None):
    instance = CurrentRm.objects.filter(id=id).first()
    form = CurrRm(request.POST or None, instance=instance)
    a = CurrentRm.objects.filter(custid=id).annotate(bid=F('bid_idA'))
    b = list(a.values_list('bid_idA', flat=True))
    try:
        rmcost13 = CurrentRm.objects.values('rmcost').get(custid=id, bid_idA=b[12])
    except IndexError:
        rmcost13 = 0
    context = {
        "instance": instance,
        "form": form,
        "rmcost13": rmcost13,
    }
    return render(request, 'wsc/room_cost13.html', context)




def conedit(request, id=None):
    instance = ContractorInfo.objects.get(id=id)
    form = Coninfo(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute_url())

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/conedit.html', context)


def addnewcust(request, id=None):
    instance = ContractorInfo.objects.get(id=id)
    form = Coninfo(request.POST or None, instance=instance)
    instance = form.save(commit=False)
    instance.save()
    a = ContractorInfo.objects.all()
    b = CustomerInfo.objects.all()
    f = JobCost.objects.all()
    t1 = a.values_list('id', flat=True).last()
    instance2 = ContractorInfo.objects.values_list('id', flat=True).get(id=id)
    c = CustomerInfo.objects.create(conid=instance2)
    g = f.create(conid=t1)
#    g = f.create(conid=instance2)
    h = f.values_list('id', flat=True).last()
    instance6 = CustomerInfo.objects.order_by('id').last()
    d = b.values_list('id', flat=True).last()
    CustomerInfo.objects.filter(id=d).update(custid=d)
    i = b.filter(id=id).update(custid=instance2)
    JobCost.objects.filter(id=h).update(jobid=h, custid=d, installtext_id=2, install='No')
#    s1 = Contract.objects.create(custid=d, conid=instance2)
    s1 = Contract.objects.create(custid=d, conid=t1)
    context2 = {
        "instance2": instance2,
        "instance6": instance6,
        "a": a,
        "b": b,
        "c": c,
        "d": d,
        "g": g,
        "i": i,
#        "s1": s1,
    }

    return redirect(instance6.get_absolute7_url(), context2)


def addcustconfirm(request, id=None):
    instance = CustomerInfo.objects.filter(id=id).last()
    form = DupConInfo(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute10_url(), context2)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/addcustconfirm.html', context)


def addcust(request, id=None):
    if request.method == 'POST':
        instance = CustomerInfo.objects.filter(id=id).last()
        form = Custinfo(request.POST or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            context2 = {
                "instance": instance,
            }
            return redirect(instance.get_absolute9_url(), context2)
        else:
            instance = CustomerInfo.objects.filter(id=id).last()
            form = Custinfo(request.POST or None, instance=instance)
            return render(request, 'wsc/custerror.html', {'form': form})
    else:
        instance = CustomerInfo.objects.filter(id=id).last()
        form = Custinfo(request.POST or None, instance=instance)
        return render(request, 'wsc/newcust.html', {'form': form})


def edit_cust_info(request, id=None):
    instance = CustomerInfo.objects.get(id=id)
    form = CustinfoC(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute5_url())

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/edit_cust_info.html', context)


def openbidpage(request, bid_idA=None):
    instance = CurrentRm.objects.get(bid_idA=bid_idA)
    form = CurrRm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute_url12())

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def bidpage(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    instance2 = get_object_or_404(BidTbl2, idA=id)
    form = BidPage(request.POST or None, instance=instance)
    form2 = BidPage2(request.POST or None, instance=instance2)
    room = RoomChoiceField
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute_url())
    context = {
        "instance": instance,
        "instance2": instance2,
        "form": form,
        "form2": form2,
        "room": room,
    }
    return render(request, 'wsc/bidpage.html', context)



def bidpage2(request, id=None):
    instance = BidTbl.objects.get(bid_idA=id)
    form = BidPage(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute_url())

    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'wsc/bidpage.html', context)


def room(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = request.POST['id_room']
    BidTbl.objects.filter(id=id).update(room_id=a)
    TotalRoomCost.objects.filter(bid_idA=id).update(room=a)
    b = BidTbl.objects.values_list('custid', flat=True).get(bid_idA=id)
    c = BidTbl.objects.filter(custid=b, room=a).count()
    d = BidTbl.objects.filter(bid_idA=id).update(roomadd=c)
    e = CurrentRm.objects.filter(bid_idA=id).update(rmnum_id=a)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute11_url())
    context = {
        "instance": instance,
        "form": form,
        "d": d,
        "e": e,
    }
    return render(request, 'wsc/bidpage.html', context)


def load_roomadd(request, id=None):
    a = BidTbl.objects.all()
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    room_add = a.values('roomadd').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute11_url())
    context = {
        "instance": instance,
        "room_add": room_add,
        "form": form,
    }
    return render(request, 'wsc/room_add.html', context)





def rmerror(request):
    return render(request, 'wsc/rmerror.html')


def rmmodal(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    instance2 = get_object_or_404(BidTbl2, id=id)
    form2 = BidPage2(request.POST or None, instance=instance)
    BidTbl.objects.filter(id=id).update(room_id='')
    context = {
        "instance": instance,
        "form": form,
        "instance2": instance2,
        "form2": form2,
    }
    return render(request, 'wsc/bidpage.html', context)


def addrm1(request, id=None):
    instance = get_object_or_404(BidTbl, bid_idA=id)
    form = BidPage(request.POST or None, instance=instance)
    a = request.POST['id_roomadd2']
    b = BidTbl.objects.filter(bid_idA=id).update(roomadd2=a)
    c = BidTbl.objects.values_list('roomadd2', flat=True).get(bid_idA=id)
    d = RoomType.objects.create(room_type=c)
    e = RoomType.objects.values_list('id', flat=True).last()
    f = RoomType.objects.filter(id=e).update(idA=e)
    g = BidTbl.objects.filter(bid_idA=id).update(room_id=e)
    h = CurrentRm.objects.filter(bid_idA=id).update(rmnum_id=e)
    i = TotalRoomCost.objects.filter(bid_idA=id).update(room_id=e)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute11_url())
    context = {
        "instance": instance,
        "form": form,
        "b": b,
        "d": d,
        "f": f,
        "g": g,
        "h": h,
        "i": i,

    }
    return render(request, 'wsc/bidpage.html', context)


def load_room(request, id=None):
    a = BidTbl.objects.all()
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    instance2 = get_object_or_404(BidTbl2, id=id)
    form2 = BidPage2(request.POST or None, instance=instance)
    b = a.values_list('room_id', flat=True).get(id=id)
    c = RoomType.objects.all().order_by("id")
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute11_url())
    context = {
        "instance": instance,
        "instance2": instance2,
        "b": b,
        "c": c,
        "form": form,
        "form2": form2,
    }
    return render(request, 'wsc/room_dropdown.html', context)


def cab1num(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_cab1num']
    BidTbl.objects.filter(id=id).update(cab1num_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab1(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_cab1']
    BidTbl.objects.filter(id=id).update(cab1_id=d, price=1)
#    a = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
#    c = BidTbl.objects.values_list('custid', flat=True).get(id=id)
#    e = BidTbl.objects.values_list('conid', flat=True).get(id=id)
#    f = BidTbl.objects.values_list('cab1_id', flat=True).get(id=id)
#    f1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
#    g = ContractInclude.objects.create(idA=id, custid=c, conid=e, bid_idA=f1, pageid=a, ident=1, qty=f, name='Ft. of Cabinets',
#                                       includeid=00, rmactive=1)
    context = {
        "instance": instance,
        "form": form,
#        "g": g,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecab1(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c = BidTbl.objects.values_list('custid', flat=True).get(id=id)
    e = BidTbl.objects.values_list('conid', flat=True).get(id=id)
    f1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    g = ContractInclude.objects.filter(idA=id, custid=c, conid=e, bid_idA=f1, pageid=a, ident=1). delete()
    context = {
        "instance": instance,
        "form": form,
        "g": g,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab1A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_cab1']
    BidTbl.objects.filter(id=id).update(cab1_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab1sides(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_cab1sides']
    BidTbl.objects.filter(id=id).update(cab1sides_id=d, price=1)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab1sidesA(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_cab1sides']
    BidTbl.objects.filter(id=id).update(cab1sides_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def drwer1A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_drwer1']
    BidTbl.objects.filter(id=id).update(drwer1_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def drwer1(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_drwer1']
    BidTbl.objects.filter(id=id).update(drwer1_id=d, price=1)
    a = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    b = ContractInclude.objects.filter(idA=id, ident=1, pageid=a).delete()
    c = BidTbl.objects.values_list('custid', flat=True).get(id=id)
    e = BidTbl.objects.values_list('conid', flat=True).get(id=id)
    f = BidTbl.objects.values_list('drwer1_id', flat=True).get(id=id)
    f1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    g = ContractInclude.objects.create(idA=id, custid=c, conid=e, bid_idA=f1, pageid=a, ident=1, qty=f, name='Drawer',
                                       includeid=0, rmactive=1)
    context = {
        "instance": instance,
        "form": form,
        "b": b,
        "g": g,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletedrwer1(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    b = ContractInclude.objects.filter(idA=id, ident=1, pageid=a).delete()
    context = {
        "instance": instance,
        "form": form,
        "b": b,
    }
    return render(request, 'wsc/bidpage.html', context)


def c11qty(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_c11qty']
    BidTbl.objects.filter(id=id).update(c11qty_id=d)
    a = CompOption.objects.values_list('price', flat=True).get(ident=11, bidid=id)
    b = int(d)
    c = int(a)
    e = b * c
    f = CompOption.objects.values_list('labor', flat=True).get(ident=11, bidid=id)
    g = int(f)
    h = b * g
    CompOption.objects.filter(ident=11, bidid=id).update(compqty=d, totalprice=e, totallabor=h)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    g1 = ContractInclude.objects.filter(idA=id, ident=11, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c11qtyA(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=id, ident=11).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c12qty(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_c12qty']
    BidTbl.objects.filter(id=id).update(c12qty_id=d)
    a = CompOption.objects.values_list('price', flat=True).get(ident=12, bidid=id)
    b = int(d)
    c = int(a)
    e = b * c
    f = CompOption.objects.values_list('labor', flat=True).get(ident=12, bidid=id)
    g = int(f)
    h = b * g
    CompOption.objects.filter(ident=12, bidid=id).update(compqty=d, totalprice=e, totallabor=h)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    g1 = ContractInclude.objects.filter(idA=id, ident=12, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c12qtyA(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=id, ident=12).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c13qty(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_c13qty']
    BidTbl.objects.filter(id=id).update(c13qty_id=d)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    a = AccOption.objects.values_list('price', flat=True).get(ident=13, bid_idA=t1, pageid=b1)
    b = int(d)
    c = int(a)
    e = b * c
    AccOption.objects.filter(ident=13, bid_idA=t1, pageid=b1).update(accqty=d, totalprice=e)

    g1 = ContractInclude.objects.filter(idA=id, ident=13, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c13qtyA(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    a = AccOption.objects.all()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    a.filter(bid_idA=t1, ident=13, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c14qty(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_c14qty']
    BidTbl.objects.filter(id=id).update(c14qty_id=d)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    a = AccOption.objects.values_list('price', flat=True).get(ident=14, bid_idA=t1, pageid=b1)
    b = int(d)
    c = int(a)
    e = b * c
    AccOption.objects.filter(ident=14, bid_idA=t1, pageid=b1).update(accqty=d, totalprice=e)

    g1 = ContractInclude.objects.filter(idA=id, ident=14, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c14qtyA(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    a = AccOption.objects.all()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    a.filter(bid_idA=t1, ident=14, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c15qty(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_c15qty']
    BidTbl.objects.filter(id=id).update(c15qty_id=d)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    a = AccOption.objects.values_list('price', flat=True).get(ident=15, bid_idA=t1, pageid=b1)
    b = int(d)
    c = int(a)
    e = b * c
    AccOption.objects.filter(ident=15, bid_idA=t1, pageid=b1).update(accqty=d, totalprice=e)

    g1 = ContractInclude.objects.filter(idA=id, ident=15, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c15qtyA(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    a = AccOption.objects.all()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    a.filter(bid_idA=t1, ident=15, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp11A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp11']
    BidTbl.objects.filter(id=id).update(comp11_id=d, c11qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp11(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp11']
    BidTbl.objects.filter(id=id).update(comp11_id=d, c11qty_id='', price=1)
    e = BidTbl.objects.all()
    f = CompOption.objects.all()
    g = e.values_list('bid_idA', flat=True).get(id=id)
    h = e.values_list('custid', flat=True).get(id=id)
    i = e.values_list('conid', flat=True).get(id=id)
    j = e.values_list('saleid', flat=True).get(id=id)
    t1 = e.values_list('room_id', flat=True).get(id=id)
    k = Comp.objects.all()
    l = k.values_list('price', flat=True).get(id=d)
    m = k.values_list('labor', flat=True).get(id=d)
    v = CompOption.objects.create(bidid=id, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t1, comp=d, ident=11,
                                  price=l, labor=m)
    f1 = Comp.objects.all()
    f2 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    c = Comp.objects.values_list('comp_type', flat=True).get(id=d)
    c1 = CompOption.objects.filter(bidid=id, comp=d).update(compname=c)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    g1 = ContractInclude.objects.create(idA=id, custid=h, conid=i, bid_idA=f2, pageid=b1, ident=11, name=c, includeid=d, rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "f1": f1,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp11(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=id, ident=11).delete()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c = ContractInclude.objects.filter(idA=id, ident=11, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp11A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=id, ident=11).delete()
    BidTbl.objects.filter(id=id).update(comp11_id='', c11qty_id='')
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    g1 = ContractInclude.objects.filter(idA=id, ident=11, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp12A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp12']
    BidTbl.objects.filter(id=id).update(comp12_id=d, c12qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp12(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp12']
    BidTbl.objects.filter(id=id).update(comp12_id=d, price=1)
    e = BidTbl.objects.all()
    f = CompOption.objects.all()
    g = e.values_list('bid_idA', flat=True).get(id=id)
    h = e.values_list('custid', flat=True).get(id=id)
    i = e.values_list('conid', flat=True).get(id=id)
    j = e.values_list('saleid', flat=True).get(id=id)
    t1 = e.values_list('room_id', flat=True).get(id=id)
    k = Comp.objects.all()
    l = k.values_list('price', flat=True).get(id=d)
    m = k.values_list('labor', flat=True).get(id=d)
    v = CompOption.objects.create(bidid=id, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t1, comp=d, ident=12,
                                  price=l, labor=m)
    f1 = Comp.objects.all()
    f2 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    c = Comp.objects.values_list('comp_type', flat=True).get(id=d)
    c1 = CompOption.objects.filter(bidid=id, comp=d).update(compname=c)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    g1 = ContractInclude.objects.create(idA=id, custid=h, conid=i, bid_idA=f2, pageid=b1, ident=12, name=c, includeid=d, rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "f1": f1,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp12(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=id, ident=12).delete()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c = ContractInclude.objects.filter(idA=id, ident=12, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp12A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=id, ident=12).delete()
    BidTbl.objects.filter(id=id).update(comp12_id='', c12qty_id='')
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    g1 = ContractInclude.objects.filter(idA=id, ident=12, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp13A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp13']
    BidTbl.objects.filter(id=id).update(comp13_id=d, c13qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp13(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp13']
    BidTbl.objects.filter(id=id).update(comp13_id=d, c13qty_id='', price=1)
    e = BidTbl.objects.all()
    f = AccOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=id)
    g = e.values_list('bid_idA', flat=True).get(id=id)
    h = e.values_list('custid', flat=True).get(id=id)
    i = e.values_list('conid', flat=True).get(id=id)
    j = e.values_list('saleid', flat=True).get(id=id)
    t2 = e.values_list('room_id', flat=True).get(id=id)
    k = CabAcc.objects.all()
    l = k.values_list('price', flat=True).get(id=d)
    f4 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    v = AccOption.objects.create(idA=id, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, acc=d,
                                 ident=13, price=l)
    c = CabAcc.objects.values_list('cabacc_type', flat=True).get(id=d)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c1 = AccOption.objects.filter(idA=id, acc=d, pageid=b1).update(accname=c)
    g1 = ContractInclude.objects.create(idA=id, custid=h, conid=i, bid_idA=f4, pageid=b1, ident=13, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp13(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c = ContractInclude.objects.filter(idA=id, ident=13, pageid=b).delete()
    d = AccOption.objects.filter(idA=id, ident=13, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "d": d,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp13A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    a.filter(bid_idA=t1, ident=13, pageid=b1).delete()
    BidTbl.objects.filter(id=id).update(comp13_id='', c13qty_id='')

    g1 = ContractInclude.objects.filter(idA=id, ident=13, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp14A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp14']
    BidTbl.objects.filter(id=id).update(comp14_id=d, c14qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp14(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp14']
    BidTbl.objects.filter(id=id).update(comp14_id=d, c14qty_id='', price=1)
    e = BidTbl.objects.all()
    f = AccOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=id)
    g = e.values_list('bid_idA', flat=True).get(id=id)
    h = e.values_list('custid', flat=True).get(id=id)
    i = e.values_list('conid', flat=True).get(id=id)
    j = e.values_list('saleid', flat=True).get(id=id)
    t2 = e.values_list('room_id', flat=True).get(id=id)
    k = CabAcc.objects.all()
    l = k.values_list('price', flat=True).get(id=d)
    f4 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    v = AccOption.objects.create(idA=id, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, acc=d,
                                 ident=14, price=l)
    c = CabAcc.objects.values_list('cabacc_type', flat=True).get(id=d)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c1 = AccOption.objects.filter(idA=id, acc=d, pageid=b1).update(accname=c)
    g1 = ContractInclude.objects.create(idA=id, custid=h, conid=i, bid_idA=f4, pageid=b1, ident=14, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp14(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c = ContractInclude.objects.filter(idA=id, ident=14, pageid=b).delete()
    d = AccOption.objects.filter(idA=id, ident=14, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "d": d,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp14A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    a.filter(bid_idA=t1, ident=14, pageid=b1).delete()
    BidTbl.objects.filter(id=id).update(comp14_id='', c14qty_id='')

    g1 = ContractInclude.objects.filter(idA=id, ident=14, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp15A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp15']
    BidTbl.objects.filter(id=id).update(comp15_id=d, c15qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp15(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp15']
    BidTbl.objects.filter(id=id).update(comp15_id=d, c15qty_id='', price=1)
    e = BidTbl.objects.all()
    f = AccOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=id)
    g = e.values_list('bid_idA', flat=True).get(id=id)
    h = e.values_list('custid', flat=True).get(id=id)
    i = e.values_list('conid', flat=True).get(id=id)
    j = e.values_list('saleid', flat=True).get(id=id)
    t2 = e.values_list('room_id', flat=True).get(id=id)
    k = CabAcc.objects.all()
    l = k.values_list('price', flat=True).get(id=d)
    f4 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    v = AccOption.objects.create(idA=id, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, acc=d,
                                 ident=15, price=l)
    c = CabAcc.objects.values_list('cabacc_type', flat=True).get(id=d)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c1 = AccOption.objects.filter(idA=id, acc=d, pageid=b1).update(accname=c)
    g1 = ContractInclude.objects.create(idA=id, custid=h, conid=i, bid_idA=f4, pageid=b1, ident=15, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp15(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c = ContractInclude.objects.filter(idA=id, ident=15, pageid=b).delete()
    d = AccOption.objects.filter(idA=id, ident=15, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "d": d,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp15A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    a.filter(bid_idA=t1, ident=15, pageid=b1).delete()
    BidTbl.objects.filter(id=id).update(comp15_id='', c15qty_id='')

    g1 = ContractInclude.objects.filter(idA=id, ident=15, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab2num(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_cab2num']
    BidTbl.objects.filter(id=id).update(cab2num_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab2(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_cab2']
    BidTbl.objects.filter(id=id).update(cab2_id=d, price=1)
#    a = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
#    c = BidTbl.objects.values_list('custid', flat=True).get(id=id)
#    e = BidTbl.objects.values_list('conid', flat=True).get(id=id)
#    f = BidTbl.objects.values_list('cab2_id', flat=True).get(id=id)
#    f1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
#    g = ContractInclude.objects.create(idA=id, custid=c, conid=e, bid_idA=f1, pageid=a, ident=2, qty=f, name='Ft. of Cabinets',
#                                       includeid=00, rmactive=1)
    context = {
        "instance": instance,
        "form": form,
#        "g": g,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecab2(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c = BidTbl.objects.values_list('custid', flat=True).get(id=id)
    e = BidTbl.objects.values_list('conid', flat=True).get(id=id)
    f1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    g = ContractInclude.objects.filter(idA=id, custid=c, conid=e, bid_idA=f1, pageid=a, ident=2). delete()
    context = {
        "instance": instance,
        "form": form,
        "g": g,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab2A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_cab2']
    BidTbl.objects.filter(id=id).update(cab2_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab2sides(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_cab2sides']
    BidTbl.objects.filter(id=id).update(cab2sides_id=d, price=1)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab2sidesA(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_cab2sides']
    BidTbl.objects.filter(id=id).update(cab2sides_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def drwer2A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_drwer2']
    BidTbl.objects.filter(id=id).update(drwer2_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def drwer2(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_drwer2']
    BidTbl.objects.filter(id=id).update(drwer2_id=d, price=1)
    a = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    b = ContractInclude.objects.filter(idA=id, ident=2, pageid=a).delete()
    c = BidTbl.objects.values_list('custid', flat=True).get(id=id)
    e = BidTbl.objects.values_list('conid', flat=True).get(id=id)
    f = BidTbl.objects.values_list('drwer2_id', flat=True).get(id=id)
    f1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    g = ContractInclude.objects.create(idA=id, custid=c, conid=e, bid_idA=f1, pageid=a, ident=2, qty=f, name='Drawer',
                                       includeid=0, rmactive=1)
    context = {
        "instance": instance,
        "form": form,
        "b": b,
        "g": g,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletedrwer2(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    b = ContractInclude.objects.filter(idA=id, ident=2, pageid=a).delete()
    context = {
        "instance": instance,
        "form": form,
        "b": b,
    }
    return render(request, 'wsc/bidpage.html', context)


def c21qty(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_c21qty']
    BidTbl.objects.filter(id=id).update(c21qty_id=d)
    a = CompOption.objects.values_list('price', flat=True).get(ident=21, bidid=id)
    b = int(d)
    c = int(a)
    e = b * c
    f = CompOption.objects.values_list('labor', flat=True).get(ident=21, bidid=id)
    g = int(f)
    h = b * g
    CompOption.objects.filter(ident=21, bidid=id).update(compqty=d, totalprice=e, totallabor=h)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    g1 = ContractInclude.objects.filter(idA=id, ident=21, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c21qtyA(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=id, ident=21).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c22qty(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_c22qty']
    BidTbl.objects.filter(id=id).update(c22qty_id=d)
    a = CompOption.objects.values_list('price', flat=True).get(ident=22, bidid=id)
    b = int(d)
    c = int(a)
    e = b * c
    f = CompOption.objects.values_list('labor', flat=True).get(ident=22, bidid=id)
    g = int(f)
    h = b * g
    CompOption.objects.filter(ident=22, bidid=id).update(compqty=d, totalprice=e, totallabor=h)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    g1 = ContractInclude.objects.filter(idA=id, ident=22, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c22qtyA(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=id, ident=22).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c23qty(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_c23qty']
    BidTbl.objects.filter(id=id).update(c23qty_id=d)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    a = AccOption.objects.values_list('price', flat=True).get(ident=23, bid_idA=t1, pageid=b1)
    b = int(d)
    c = int(a)
    e = b * c
    AccOption.objects.filter(ident=23, bid_idA=t1, pageid=b1).update(accqty=d, totalprice=e)

    g1 = ContractInclude.objects.filter(idA=id, ident=23, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c23qtyA(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    a = AccOption.objects.all()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    a.filter(bid_idA=t1, ident=23, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c24qty(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_c24qty']
    BidTbl.objects.filter(id=id).update(c24qty_id=d)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    a = AccOption.objects.values_list('price', flat=True).get(ident=24, bid_idA=t1, pageid=b1)
    b = int(d)
    c = int(a)
    e = b * c
    AccOption.objects.filter(ident=24, bid_idA=t1, pageid=b1).update(accqty=d, totalprice=e)

    g1 = ContractInclude.objects.filter(idA=id, ident=24, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c24qtyA(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    a = AccOption.objects.all()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    a.filter(bid_idA=t1, ident=24, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c25qty(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_c25qty']
    BidTbl.objects.filter(id=id).update(c25qty_id=d)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    a = AccOption.objects.values_list('price', flat=True).get(ident=25, bid_idA=t1, pageid=b1)
    b = int(d)
    c = int(a)
    e = b * c
    AccOption.objects.filter(ident=25, bid_idA=t1, pageid=b1).update(accqty=d, totalprice=e)

    g1 = ContractInclude.objects.filter(idA=id, ident=25, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c25qtyA(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    a = AccOption.objects.all()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    a.filter(bid_idA=t1, ident=25, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp21A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp21']
    BidTbl.objects.filter(id=id).update(comp21_id=d, c21qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp21(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp21']
    BidTbl.objects.filter(id=id).update(comp21_id=d, c21qty_id='', price=1)
    e = BidTbl.objects.all()
    f = CompOption.objects.all()
    g = e.values_list('bid_idA', flat=True).get(id=id)
    h = e.values_list('custid', flat=True).get(id=id)
    i = e.values_list('conid', flat=True).get(id=id)
    j = e.values_list('saleid', flat=True).get(id=id)
    t1 = e.values_list('room_id', flat=True).get(id=id)
    k = Comp.objects.all()
    l = k.values_list('price', flat=True).get(id=d)
    m = k.values_list('labor', flat=True).get(id=d)
    v = CompOption.objects.create(bidid=id, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t1, comp=d, ident=21,
                                  price=l, labor=m)
    f1 = Comp.objects.all()
    f2 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    c = Comp.objects.values_list('comp_type', flat=True).get(id=d)
    c1 = CompOption.objects.filter(bidid=id, comp=d).update(compname=c)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    g1 = ContractInclude.objects.create(idA=id, custid=h, conid=i, bid_idA=f2, pageid=b1, ident=21, name=c, includeid=d, rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "f1": f1,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp21(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=id, ident=21).delete()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c = ContractInclude.objects.filter(idA=id, ident=21, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp21A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=id, ident=21).delete()
    BidTbl.objects.filter(id=id).update(comp21_id='', c21qty_id='')
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    g1 = ContractInclude.objects.filter(idA=id, ident=21, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp22A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp22']
    BidTbl.objects.filter(id=id).update(comp22_id=d, c22qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp22(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp22']
    BidTbl.objects.filter(id=id).update(comp22_id=d, price=1)
    e = BidTbl.objects.all()
    f = CompOption.objects.all()
    g = e.values_list('bid_idA', flat=True).get(id=id)
    h = e.values_list('custid', flat=True).get(id=id)
    i = e.values_list('conid', flat=True).get(id=id)
    j = e.values_list('saleid', flat=True).get(id=id)
    t1 = e.values_list('room_id', flat=True).get(id=id)
    k = Comp.objects.all()
    l = k.values_list('price', flat=True).get(id=d)
    m = k.values_list('labor', flat=True).get(id=d)
    v = CompOption.objects.create(bidid=id, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t1, comp=d, ident=22,
                                  price=l, labor=m)
    f1 = Comp.objects.all()
    f2 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    c = Comp.objects.values_list('comp_type', flat=True).get(id=d)
    c1 = CompOption.objects.filter(bidid=id, comp=d).update(compname=c)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    g1 = ContractInclude.objects.create(idA=id, custid=h, conid=i, bid_idA=f2, pageid=b1, ident=22, name=c, includeid=d, rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "f1": f1,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp22(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=id, ident=22).delete()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c = ContractInclude.objects.filter(idA=id, ident=22, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp22A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=id, ident=22).delete()
    BidTbl.objects.filter(id=id).update(comp22_id='', c22qty_id='')
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    g1 = ContractInclude.objects.filter(idA=id, ident=22, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp23A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp23']
    BidTbl.objects.filter(id=id).update(comp23_id=d, c23qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp23(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp23']
    BidTbl.objects.filter(id=id).update(comp23_id=d, c23qty_id='', price=1)
    e = BidTbl.objects.all()
    f = AccOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=id)
    g = e.values_list('bid_idA', flat=True).get(id=id)
    h = e.values_list('custid', flat=True).get(id=id)
    i = e.values_list('conid', flat=True).get(id=id)
    j = e.values_list('saleid', flat=True).get(id=id)
    t2 = e.values_list('room_id', flat=True).get(id=id)
    k = CabAcc.objects.all()
    l = k.values_list('price', flat=True).get(id=d)
    f4 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    v = AccOption.objects.create(idA=id, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, acc=d,
                                 ident=23, price=l)
    c = CabAcc.objects.values_list('cabacc_type', flat=True).get(id=d)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c1 = AccOption.objects.filter(idA=id, acc=d, pageid=b1).update(accname=c)
    g1 = ContractInclude.objects.create(idA=id, custid=h, conid=i, bid_idA=f4, pageid=b1, ident=23, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp23(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c = ContractInclude.objects.filter(idA=id, ident=23, pageid=b).delete()
    d = AccOption.objects.filter(idA=id, ident=23, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "d": d,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp23A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    a.filter(bid_idA=t1, ident=23, pageid=b1).delete()
    BidTbl.objects.filter(id=id).update(comp23_id='', c23qty_id='')

    g1 = ContractInclude.objects.filter(idA=id, ident=23, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp24A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp24']
    BidTbl.objects.filter(id=id).update(comp24_id=d, c24qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp24(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp24']
    BidTbl.objects.filter(id=id).update(comp24_id=d, c24qty_id='', price=1)
    e = BidTbl.objects.all()
    f = AccOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=id)
    g = e.values_list('bid_idA', flat=True).get(id=id)
    h = e.values_list('custid', flat=True).get(id=id)
    i = e.values_list('conid', flat=True).get(id=id)
    j = e.values_list('saleid', flat=True).get(id=id)
    t2 = e.values_list('room_id', flat=True).get(id=id)
    k = CabAcc.objects.all()
    l = k.values_list('price', flat=True).get(id=d)
    f4 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    v = AccOption.objects.create(idA=id, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, acc=d,
                                 ident=24, price=l)
    c = CabAcc.objects.values_list('cabacc_type', flat=True).get(id=d)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c1 = AccOption.objects.filter(idA=id, acc=d, pageid=b1).update(accname=c)
    g1 = ContractInclude.objects.create(idA=id, custid=h, conid=i, bid_idA=f4, pageid=b1, ident=24, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp24(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c = ContractInclude.objects.filter(idA=id, ident=24, pageid=b).delete()
    d = AccOption.objects.filter(idA=id, ident=24, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "d": d,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp24A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    a.filter(bid_idA=t1, ident=24, pageid=b1).delete()
    BidTbl.objects.filter(id=id).update(comp24_id='', c24qty_id='')

    g1 = ContractInclude.objects.filter(idA=id, ident=24, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp25A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp25']
    BidTbl.objects.filter(id=id).update(comp25_id=d, c25qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp25(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp25']
    BidTbl.objects.filter(id=id).update(comp25_id=d, c25qty_id='', price=1)
    e = BidTbl.objects.all()
    f = AccOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=id)
    g = e.values_list('bid_idA', flat=True).get(id=id)
    h = e.values_list('custid', flat=True).get(id=id)
    i = e.values_list('conid', flat=True).get(id=id)
    j = e.values_list('saleid', flat=True).get(id=id)
    t2 = e.values_list('room_id', flat=True).get(id=id)
    k = CabAcc.objects.all()
    l = k.values_list('price', flat=True).get(id=d)
    f4 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    v = AccOption.objects.create(idA=id, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, acc=d,
                                 ident=25, price=l)
    c = CabAcc.objects.values_list('cabacc_type', flat=True).get(id=d)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c1 = AccOption.objects.filter(idA=id, acc=d, pageid=b1).update(accname=c)
    g1 = ContractInclude.objects.create(idA=id, custid=h, conid=i, bid_idA=f4, pageid=b1, ident=25, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp25(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c = ContractInclude.objects.filter(idA=id, ident=25, pageid=b).delete()
    d = AccOption.objects.filter(idA=id, ident=25, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "d": d,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp25A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    a.filter(bid_idA=t1, ident=25, pageid=b1).delete()
    BidTbl.objects.filter(id=id).update(comp25_id='', c25qty_id='')

    g1 = ContractInclude.objects.filter(idA=id, ident=25, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab3num(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_cab3num']
    BidTbl.objects.filter(id=id).update(cab3num_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab3(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_cab3']
    BidTbl.objects.filter(id=id).update(cab3_id=d, price=1)
#    a = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
#    c = BidTbl.objects.values_list('custid', flat=True).get(id=id)
#    e = BidTbl.objects.values_list('conid', flat=True).get(id=id)
#    f = BidTbl.objects.values_list('cab3_id', flat=True).get(id=id)
#    f1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
#    g = ContractInclude.objects.create(idA=id, custid=c, conid=e, bid_idA=f1, pageid=a, ident=3, qty=f, name='Ft. of Cabinets',
#                                       includeid=00, rmactive=1)
    context = {
        "instance": instance,
        "form": form,
#        "g": g,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecab3(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c = BidTbl.objects.values_list('custid', flat=True).get(id=id)
    e = BidTbl.objects.values_list('conid', flat=True).get(id=id)
    f1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    g = ContractInclude.objects.filter(idA=id, custid=c, conid=e, bid_idA=f1, pageid=a, ident=3). delete()
    context = {
        "instance": instance,
        "form": form,
        "g": g,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab3A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_cab3']
    BidTbl.objects.filter(id=id).update(cab3_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab3sides(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_cab3sides']
    BidTbl.objects.filter(id=id).update(cab3sides_id=d, price=1)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab3sidesA(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_cab3sides']
    BidTbl.objects.filter(id=id).update(cab3sides_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def drwer3A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_drwer3']
    BidTbl.objects.filter(id=id).update(drwer3_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def drwer3(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_drwer3']
    BidTbl.objects.filter(id=id).update(drwer3_id=d, price=1)
    a = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    b = ContractInclude.objects.filter(idA=id, ident=3, pageid=a).delete()
    c = BidTbl.objects.values_list('custid', flat=True).get(id=id)
    e = BidTbl.objects.values_list('conid', flat=True).get(id=id)
    f = BidTbl.objects.values_list('drwer3_id', flat=True).get(id=id)
    f1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    g = ContractInclude.objects.create(idA=id, custid=c, conid=e, bid_idA=f1, pageid=a, ident=3, qty=f, name='Drawer',
                                       includeid=0, rmactive=1)
    context = {
        "instance": instance,
        "form": form,
        "b": b,
        "g": g,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletedrwer3(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    b = ContractInclude.objects.filter(idA=id, ident=3, pageid=a).delete()
    context = {
        "instance": instance,
        "form": form,
        "b": b,
    }
    return render(request, 'wsc/bidpage.html', context)


def c31qty(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_c31qty']
    BidTbl.objects.filter(id=id).update(c31qty_id=d)
    a = CompOption.objects.values_list('price', flat=True).get(ident=31, bidid=id)
    b = int(d)
    c = int(a)
    e = b * c
    f = CompOption.objects.values_list('labor', flat=True).get(ident=31, bidid=id)
    g = int(f)
    h = b * g
    CompOption.objects.filter(ident=31, bidid=id).update(compqty=d, totalprice=e, totallabor=h)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    g1 = ContractInclude.objects.filter(idA=id, ident=31, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c31qtyA(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=id, ident=31).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c32qty(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_c32qty']
    BidTbl.objects.filter(id=id).update(c32qty_id=d)
    a = CompOption.objects.values_list('price', flat=True).get(ident=32, bidid=id)
    b = int(d)
    c = int(a)
    e = b * c
    f = CompOption.objects.values_list('labor', flat=True).get(ident=32, bidid=id)
    g = int(f)
    h = b * g
    CompOption.objects.filter(ident=32, bidid=id).update(compqty=d, totalprice=e, totallabor=h)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    g1 = ContractInclude.objects.filter(idA=id, ident=32, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c32qtyA(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=id, ident=32).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c33qty(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_c33qty']
    BidTbl.objects.filter(id=id).update(c33qty_id=d)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    a = AccOption.objects.values_list('price', flat=True).get(ident=33, bid_idA=t1, pageid=b1)
    b = int(d)
    c = int(a)
    e = b * c
    AccOption.objects.filter(ident=33, bid_idA=t1, pageid=b1).update(accqty=d, totalprice=e)

    g1 = ContractInclude.objects.filter(idA=id, ident=33, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c33qtyA(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    a = AccOption.objects.all()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    a.filter(bid_idA=t1, ident=33, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c34qty(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_c34qty']
    BidTbl.objects.filter(id=id).update(c34qty_id=d)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    a = AccOption.objects.values_list('price', flat=True).get(ident=34, bid_idA=t1, pageid=b1)
    b = int(d)
    c = int(a)
    e = b * c
    AccOption.objects.filter(ident=34, bid_idA=t1, pageid=b1).update(accqty=d, totalprice=e)

    g1 = ContractInclude.objects.filter(idA=id, ident=34, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c34qtyA(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    a = AccOption.objects.all()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    a.filter(bid_idA=t1, ident=34, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c35qty(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_c35qty']
    BidTbl.objects.filter(id=id).update(c35qty_id=d)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    a = AccOption.objects.values_list('price', flat=True).get(ident=35, bid_idA=t1, pageid=b1)
    b = int(d)
    c = int(a)
    e = b * c
    AccOption.objects.filter(ident=35, bid_idA=t1, pageid=b1).update(accqty=d, totalprice=e)

    g1 = ContractInclude.objects.filter(idA=id, ident=35, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c35qtyA(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    a = AccOption.objects.all()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    a.filter(bid_idA=t1, ident=35, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp31A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp31']
    BidTbl.objects.filter(id=id).update(comp31_id=d, c31qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp31(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp31']
    BidTbl.objects.filter(id=id).update(comp31_id=d, c31qty_id='', price=1)
    e = BidTbl.objects.all()
    f = CompOption.objects.all()
    g = e.values_list('bid_idA', flat=True).get(id=id)
    h = e.values_list('custid', flat=True).get(id=id)
    i = e.values_list('conid', flat=True).get(id=id)
    j = e.values_list('saleid', flat=True).get(id=id)
    t1 = e.values_list('room_id', flat=True).get(id=id)
    k = Comp.objects.all()
    l = k.values_list('price', flat=True).get(id=d)
    m = k.values_list('labor', flat=True).get(id=d)
    v = CompOption.objects.create(bidid=id, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t1, comp=d, ident=31,
                                  price=l, labor=m)
    f1 = Comp.objects.all()
    f2 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    c = Comp.objects.values_list('comp_type', flat=True).get(id=d)
    c1 = CompOption.objects.filter(bidid=id, comp=d).update(compname=c)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    g1 = ContractInclude.objects.create(idA=id, custid=h, conid=i, bid_idA=f2, pageid=b1, ident=31, name=c, includeid=d, rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "f1": f1,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp31(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=id, ident=31).delete()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c = ContractInclude.objects.filter(idA=id, ident=31, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp31A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=id, ident=31).delete()
    BidTbl.objects.filter(id=id).update(comp31_id='', c31qty_id='')
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    g1 = ContractInclude.objects.filter(idA=id, ident=31, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp32A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp32']
    BidTbl.objects.filter(id=id).update(comp32_id=d, c32qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp32(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp32']
    BidTbl.objects.filter(id=id).update(comp32_id=d, price=1)
    e = BidTbl.objects.all()
    f = CompOption.objects.all()
    g = e.values_list('bid_idA', flat=True).get(id=id)
    h = e.values_list('custid', flat=True).get(id=id)
    i = e.values_list('conid', flat=True).get(id=id)
    j = e.values_list('saleid', flat=True).get(id=id)
    t1 = e.values_list('room_id', flat=True).get(id=id)
    k = Comp.objects.all()
    l = k.values_list('price', flat=True).get(id=d)
    m = k.values_list('labor', flat=True).get(id=d)
    v = CompOption.objects.create(bidid=id, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t1, comp=d, ident=32,
                                  price=l, labor=m)
    f1 = Comp.objects.all()
    f2 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    c = Comp.objects.values_list('comp_type', flat=True).get(id=d)
    c1 = CompOption.objects.filter(bidid=id, comp=d).update(compname=c)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    g1 = ContractInclude.objects.create(idA=id, custid=h, conid=i, bid_idA=f2, pageid=b1, ident=32, name=c, includeid=d,
                                        rmactive=1)


    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "f1": f1,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp32(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=id, ident=32).delete()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c = ContractInclude.objects.filter(idA=id, ident=32, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp32A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=id, ident=32).delete()
    BidTbl.objects.filter(id=id).update(comp32_id='', c32qty_id='')
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    g1 = ContractInclude.objects.filter(idA=id, ident=32, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp33A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp33']
    BidTbl.objects.filter(id=id).update(comp33_id=d, c33qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp33(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp33']
    BidTbl.objects.filter(id=id).update(comp33_id=d, c33qty_id='', price=1)
    e = BidTbl.objects.all()
    f = AccOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=id)
    g = e.values_list('bid_idA', flat=True).get(id=id)
    h = e.values_list('custid', flat=True).get(id=id)
    i = e.values_list('conid', flat=True).get(id=id)
    j = e.values_list('saleid', flat=True).get(id=id)
    t2 = e.values_list('room_id', flat=True).get(id=id)
    k = CabAcc.objects.all()
    l = k.values_list('price', flat=True).get(id=d)
    f4 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    v = AccOption.objects.create(idA=id, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, acc=d,
                                 ident=33, price=l)
    c = CabAcc.objects.values_list('cabacc_type', flat=True).get(id=d)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c1 = AccOption.objects.filter(idA=id, acc=d, pageid=b1).update(accname=c)
    g1 = ContractInclude.objects.create(idA=id, custid=h, conid=i, bid_idA=f4, pageid=b1, ident=33, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp33(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c = ContractInclude.objects.filter(idA=id, ident=33, pageid=b).delete()
    d = AccOption.objects.filter(idA=id, ident=33, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "d": d,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp33A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    a.filter(bid_idA=t1, ident=33, pageid=b1).delete()
    BidTbl.objects.filter(id=id).update(comp33_id='', c33qty_id='')

    g1 = ContractInclude.objects.filter(idA=id, ident=33, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp34A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp34']
    BidTbl.objects.filter(id=id).update(comp34_id=d, c34qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp34(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp34']
    BidTbl.objects.filter(id=id).update(comp34_id=d, c34qty_id='', price=1)
    e = BidTbl.objects.all()
    f = AccOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=id)
    g = e.values_list('bid_idA', flat=True).get(id=id)
    h = e.values_list('custid', flat=True).get(id=id)
    i = e.values_list('conid', flat=True).get(id=id)
    j = e.values_list('saleid', flat=True).get(id=id)
    t2 = e.values_list('room_id', flat=True).get(id=id)
    k = CabAcc.objects.all()
    l = k.values_list('price', flat=True).get(id=d)
    f4 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    v = AccOption.objects.create(idA=id, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, acc=d,
                                 ident=34, price=l)
    c = CabAcc.objects.values_list('cabacc_type', flat=True).get(id=d)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c1 = AccOption.objects.filter(idA=id, acc=d, pageid=b1).update(accname=c)
    g1 = ContractInclude.objects.create(idA=id, custid=h, conid=i, bid_idA=f4, pageid=b1, ident=34, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp34(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c = ContractInclude.objects.filter(idA=id, ident=34, pageid=b).delete()
    d = AccOption.objects.filter(idA=id, ident=34, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "d": d,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp34A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    a.filter(bid_idA=t1, ident=34, pageid=b1).delete()
    BidTbl.objects.filter(id=id).update(comp34_id='', c34qty_id='')

    g1 = ContractInclude.objects.filter(idA=id, ident=34, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp35A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp35']
    BidTbl.objects.filter(id=id).update(comp35_id=d, c35qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp35(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_comp35']
    BidTbl.objects.filter(id=id).update(comp35_id=d, c35qty_id='', price=1)
    e = BidTbl.objects.all()
    f = AccOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=id)
    g = e.values_list('bid_idA', flat=True).get(id=id)
    h = e.values_list('custid', flat=True).get(id=id)
    i = e.values_list('conid', flat=True).get(id=id)
    j = e.values_list('saleid', flat=True).get(id=id)
    t2 = e.values_list('room_id', flat=True).get(id=id)
    k = CabAcc.objects.all()
    l = k.values_list('price', flat=True).get(id=d)
    f4 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    v = AccOption.objects.create(idA=id, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, acc=d,
                                 ident=35, price=l)
    c = CabAcc.objects.values_list('cabacc_type', flat=True).get(id=d)
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c1 = AccOption.objects.filter(idA=id, acc=d, pageid=b1).update(accname=c)
    g1 = ContractInclude.objects.create(idA=id, custid=h, conid=i, bid_idA=f4, pageid=b1, ident=35, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp35(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    c = ContractInclude.objects.filter(idA=id, ident=35, pageid=b).delete()
    d = AccOption.objects.filter(idA=id, ident=35, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "d": d,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp35A(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    b1 = BidTbl.objects.values_list('pageid', flat=True).get(id=id)
    t1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    a.filter(bid_idA=t1, ident=35, pageid=b1).delete()
    BidTbl.objects.filter(id=id).update(comp35_id='', c35qty_id='')

    g1 = ContractInclude.objects.filter(idA=id, ident=35, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab4num(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_cab4num']
    BidTbl2.objects.filter(id=idA).update(cab4num_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab4(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_cab4']
    BidTbl2.objects.filter(id=idA).update(cab4_id=d, price=1)
#    a = BidTbl.objects.values_list('pageid', flat=True).get(id=idA)
#    c = BidTbl.objects.values_list('custid', flat=True).get(id=idA)
#    e = BidTbl.objects.values_list('conid', flat=True).get(id=idA)
#    f = BidTbl2.objects.values_list('cab4_id', flat=True).get(id=idA)
#    f1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=idA)
#    g = ContractInclude.objects.create(idA=idA, custid=c, conid=e, bid_idA=f1, pageid=a, ident=4, qty=f,
#                                       name='Ft. of Cabinets',
#                                       includeid=00, rmactive=1)
    context = {
        "instance": instance,
        "form": form,
#        "g": g,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecab4(request, idA=None):
    instance = get_object_or_404(BidTbl, id=idA)
    form = BidPage(request.POST or None, instance=instance)
    a = BidTbl.objects.values_list('pageid', flat=True).get(id=idA)
    c = BidTbl.objects.values_list('custid', flat=True).get(id=idA)
    e = BidTbl.objects.values_list('conid', flat=True).get(id=idA)
    f1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=idA)
    g = ContractInclude.objects.filter(idA=idA, custid=c, conid=e, bid_idA=f1, pageid=a, ident=4).delete()
    context = {
        "instance": instance,
        "form": form,
        "g": g,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab4A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_cab4']
    BidTbl2.objects.filter(id=idA).update(cab4_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab4sides(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_cab4sides']
    BidTbl2.objects.filter(id=idA).update(cab4sides_id=d, price=1)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab4sidesA(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_cab4sides']
    BidTbl2.objects.filter(id=idA).update(cab4sides_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def drwer4A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_drwer4']
    BidTbl2.objects.filter(id=idA).update(drwer4_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def drwer4(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_drwer4']
    BidTbl2.objects.filter(id=idA).update(drwer4_id=d, price=1)
    a = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    b = ContractInclude.objects.filter(idA=idA, ident=4, pageid=a).delete()
    c = BidTbl2.objects.values_list('custid', flat=True).get(id=idA)
    e = BidTbl2.objects.values_list('conid', flat=True).get(id=idA)
    f = BidTbl2.objects.values_list('drwer4_id', flat=True).get(id=idA)
    g = BidTbl2.objects.values_list('bid_idA', flat=True).get(id=idA)
    h = ContractInclude.objects.create(idA=idA, custid=c, conid=e, bid_idA=g, pageid=a, ident=4, qty=f, name='Drawer',
                                       includeid=0, rmactive=1)
    context = {
        "instance": instance,
        "form": form,
        "h": h,
        "b": b,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletedrwer4(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    b = ContractInclude.objects.filter(idA=idA, ident=4, pageid=a).delete()
    context = {
        "instance": instance,
        "form": form,
        "b": b,
    }
    return render(request, 'wsc/bidpage.html', context)


def c41qty(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_c41qty']
    BidTbl2.objects.filter(id=idA).update(c41qty_id=d)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = CompOption.objects.values_list('price', flat=True).get(ident=41, idA=t1)
    b = int(d)
    c = int(a)
    e = b * c
    f = CompOption.objects.values_list('labor', flat=True).get(ident=41, idA=t1)
    g = int(f)
    h = b * g
    CompOption.objects.filter(ident=41, idA=t1).update(compqty=d, totalprice=e, totallabor=h)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=41, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c41qtyA(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=idA, ident=41).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c42qty(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_c42qty']
    BidTbl2.objects.filter(id=idA).update(c42qty_id=d)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = CompOption.objects.values_list('price', flat=True).get(ident=42, idA=t1)
    b = int(d)
    c = int(a)
    e = b * c
    f = CompOption.objects.values_list('labor', flat=True).get(ident=42, idA=t1)
    g = int(f)
    h = b * g
    CompOption.objects.filter(ident=42, idA=t1).update(compqty=d, totalprice=e, totallabor=h)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=42, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c42qtyA(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=idA, ident=42).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c43qty(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_c43qty']
    BidTbl2.objects.filter(id=idA).update(c43qty_id=d)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = AccOption.objects.values_list('price', flat=True).get(ident=43, idA=t1)
    b = int(d)
    c = int(a)
    e = b * c
    AccOption.objects.filter(ident=43, idA=t1).update(accqty=d, totalprice=e)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=43, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c43qtyA(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    a.filter(bidid=id, ident=43).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c44qty(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_c44qty']
    BidTbl2.objects.filter(id=idA).update(c44qty_id=d)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = AccOption.objects.values_list('price', flat=True).get(ident=44, idA=t1)
    b = int(d)
    c = int(a)
    e = b * c
    AccOption.objects.filter(ident=44, idA=t1).update(accqty=d, totalprice=e)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=44, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c44qtyA(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    a.filter(bidid=id, ident=44).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c45qty(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_c45qty']
    BidTbl2.objects.filter(id=idA).update(c45qty_id=d)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = AccOption.objects.values_list('price', flat=True).get(ident=45, idA=t1)
    b = int(d)
    c = int(a)
    e = b * c
    AccOption.objects.filter(ident=45, idA=t1).update(accqty=d, totalprice=e)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=45, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c45qtyA(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    a.filter(bidid=id, ident=45).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp41A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp41']
    BidTbl2.objects.filter(id=idA).update(comp41_id=d, c41qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp41(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp41']
    BidTbl2.objects.filter(id=idA).update(comp41_id=d, c41qty_id='', price=1)
    e = BidTbl2.objects.all()
    t1 = BidTbl.objects.all()
    f = CompOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=idA)
    f3 = e.values_list('idA', flat=True).get(id=idA)
    g = e.values_list('bid_idA', flat=True).get(id=idA)
    h = e.values_list('custid', flat=True).get(id=idA)
    i = e.values_list('conid', flat=True).get(id=idA)
    j = e.values_list('saleid', flat=True).get(id=idA)
    t2 = t1.values_list('room_id', flat=True).get(id=idA)
    k = Comp.objects.all()
    l = k.values_list('price', flat=True).get(id=d)
    m = k.values_list('labor', flat=True).get(id=d)
    v = CompOption.objects.create(idA=f3, bidid=g, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, comp=d,
                                  ident=41, price=l, labor=m)
    f1 = Comp.objects.all()
    c = Comp.objects.values_list('comp_type', flat=True).get(id=d)
    c1 = CompOption.objects.filter(idA=idA, comp=d).update(compname=c)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.create(idA=idA, custid=h, conid=i, bid_idA=g, pageid=b1, ident=41, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "f2": f2,
        "f1": f1,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp41(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = CompOption.objects.all()
    a.filter(idA=t1, ident=41).delete()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=idA)
    c = ContractInclude.objects.filter(idA=idA, ident=41, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp41A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=idA, ident=41).delete()
    BidTbl2.objects.filter(id=idA).update(comp41_id='', c41qty_id='')
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(idA=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=41, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp42A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp42']
    BidTbl2.objects.filter(id=idA).update(comp42_id=d, c42qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp42(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp42']
    BidTbl2.objects.filter(id=idA).update(comp42_id=d, c42qty_id='', price=1)
    e = BidTbl2.objects.all()
    t1 = BidTbl.objects.all()
    f = CompOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=idA)
    f3 = e.values_list('idA', flat=True).get(id=idA)
    g = e.values_list('bid_idA', flat=True).get(id=idA)
    h = e.values_list('custid', flat=True).get(id=idA)
    i = e.values_list('conid', flat=True).get(id=idA)
    j = e.values_list('saleid', flat=True).get(id=idA)
    t2 = t1.values_list('room_id', flat=True).get(id=idA)
    k = Comp.objects.all()
    l = k.values_list('price', flat=True).get(id=d)
    m = k.values_list('labor', flat=True).get(id=d)
    v = CompOption.objects.create(idA=f3, bidid=g, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, comp=d,
                                  ident=42, price=l, labor=m)
    f1 = Comp.objects.all()
    c = Comp.objects.values_list('comp_type', flat=True).get(id=d)
    c1 = CompOption.objects.filter(idA=idA, comp=d).update(compname=c)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.create(idA=idA, custid=h, conid=i, bid_idA=g, pageid=b1, ident=42, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "f2": f2,
        "f1": f1,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp42(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = CompOption.objects.all()
    a.filter(idA=t1, ident=42).delete()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=idA)
    c = ContractInclude.objects.filter(idA=idA, ident=42, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp42A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=idA, ident=42).delete()
    BidTbl2.objects.filter(id=idA).update(comp42_id='', c42qty_id='')
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(idA=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=42, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp43A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp43']
    BidTbl2.objects.filter(id=idA).update(comp43_id=d, c43qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp43(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp43']
    BidTbl2.objects.filter(id=idA).update(comp43_id=d, c43qty_id='', price=1)
    e = BidTbl2.objects.all()
    t1 = BidTbl.objects.all()
    f = AccOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=idA)
    f3 = e.values_list('idA', flat=True).get(id=idA)
    g = e.values_list('bid_idA', flat=True).get(id=idA)
    h = e.values_list('custid', flat=True).get(id=idA)
    i = e.values_list('conid', flat=True).get(id=idA)
    j = e.values_list('saleid', flat=True).get(id=idA)
    t2 = t1.values_list('room_id', flat=True).get(id=idA)
    k = CabAcc.objects.all()
    f4 = BidTbl2.objects.values_list('bid_idA', flat=True).get(idA=idA)
    l = k.values_list('price', flat=True).get(id=d)
    v = AccOption.objects.create(idA=f3, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, acc=d,
                                 ident=43, price=l)
    c = CabAcc.objects.values_list('cabacc_type', flat=True).get(id=d)
    c1 = AccOption.objects.filter(idA=idA, acc=d).update(accname=c)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.create(idA=idA, custid=h, conid=i, bid_idA=f4, pageid=b1, ident=43, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp43(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = AccOption.objects.all()
    a.filter(idA=t1, ident=43).delete()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=idA)
    c = ContractInclude.objects.filter(idA=idA, ident=43, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp43A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    a.filter(bidid=idA, ident=43).delete()
    BidTbl2.objects.filter(id=idA).update(comp43_id='', c43qty_id='')
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(idA=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=43, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp44A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp44']
    BidTbl2.objects.filter(id=idA).update(comp44_id=d, c44qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp44(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp44']
    BidTbl2.objects.filter(id=idA).update(comp44_id=d, c44qty_id='', price=1)
    e = BidTbl2.objects.all()
    t1 = BidTbl.objects.all()
    f = AccOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=idA)
    f3 = e.values_list('idA', flat=True).get(id=idA)
    g = e.values_list('bid_idA', flat=True).get(id=idA)
    h = e.values_list('custid', flat=True).get(id=idA)
    i = e.values_list('conid', flat=True).get(id=idA)
    j = e.values_list('saleid', flat=True).get(id=idA)
    t2 = t1.values_list('room_id', flat=True).get(id=idA)
    k = CabAcc.objects.all()
    f4 = BidTbl2.objects.values_list('bid_idA', flat=True).get(idA=idA)
    l = k.values_list('price', flat=True).get(id=d)
    v = AccOption.objects.create(idA=f3, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, acc=d,
                                 ident=44, price=l)
    c = CabAcc.objects.values_list('cabacc_type', flat=True).get(id=d)
    c1 = AccOption.objects.filter(idA=idA, acc=d).update(accname=c)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.create(idA=idA, custid=h, conid=i, bid_idA=f4, pageid=b1, ident=44, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp44(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = AccOption.objects.all()
    a.filter(idA=t1, ident=44).delete()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=idA)
    c = ContractInclude.objects.filter(idA=idA, ident=44, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp44A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    a.filter(bidid=idA, ident=44).delete()
    BidTbl2.objects.filter(id=idA).update(comp44_id='', c44qty_id='')
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(idA=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=44, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp45A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp45']
    BidTbl2.objects.filter(id=idA).update(comp45_id=d, c45qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp45(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp45']
    BidTbl2.objects.filter(id=idA).update(comp45_id=d, c45qty_id='', price=1)
    e = BidTbl2.objects.all()
    t1 = BidTbl.objects.all()
    f = AccOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=idA)
    f3 = e.values_list('idA', flat=True).get(id=idA)
    g = e.values_list('bid_idA', flat=True).get(id=idA)
    h = e.values_list('custid', flat=True).get(id=idA)
    i = e.values_list('conid', flat=True).get(id=idA)
    j = e.values_list('saleid', flat=True).get(id=idA)
    t2 = t1.values_list('room_id', flat=True).get(id=idA)
    k = CabAcc.objects.all()
    f4 = BidTbl2.objects.values_list('bid_idA', flat=True).get(idA=idA)
    l = k.values_list('price', flat=True).get(id=d)
    v = AccOption.objects.create(idA=f3, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, acc=d,
                                 ident=45, price=l)
    c = CabAcc.objects.values_list('cabacc_type', flat=True).get(id=d)
    c1 = AccOption.objects.filter(idA=idA, acc=d).update(accname=c)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.create(idA=idA, custid=h, conid=i, bid_idA=f4, pageid=b1, ident=45, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp45(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = AccOption.objects.all()
    a.filter(idA=t1, ident=45).delete()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=idA)
    c = ContractInclude.objects.filter(idA=idA, ident=45, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp45A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    a.filter(bidid=idA, ident=45).delete()
    BidTbl2.objects.filter(id=idA).update(comp45_id='', c45qty_id='')
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(idA=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=45, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab5num(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_cab5num']
    BidTbl2.objects.filter(id=idA).update(cab5num_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab5(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_cab5']
    BidTbl2.objects.filter(id=idA).update(cab5_id=d, price=1)
#    a = BidTbl.objects.values_list('pageid', flat=True).get(id=idA)
#    c = BidTbl.objects.values_list('custid', flat=True).get(id=idA)
#    e = BidTbl.objects.values_list('conid', flat=True).get(id=idA)
#    f = BidTbl2.objects.values_list('cab5_id', flat=True).get(id=idA)
#    f1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=idA)
#    g = ContractInclude.objects.create(idA=idA, custid=c, conid=e, bid_idA=f1, pageid=a, ident=5, qty=f,
#                                       name='Ft. of Cabinets',
#                                       includeid=00, rmactive=1)
    context = {
        "instance": instance,
        "form": form,
#        "g": g,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecab5(request, idA=None):
    instance = get_object_or_404(BidTbl, id=idA)
    form = BidPage(request.POST or None, instance=instance)
    a = BidTbl.objects.values_list('pageid', flat=True).get(id=idA)
    c = BidTbl.objects.values_list('custid', flat=True).get(id=idA)
    e = BidTbl.objects.values_list('conid', flat=True).get(id=idA)
    f1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=idA)
    g = ContractInclude.objects.filter(idA=idA, custid=c, conid=e, bid_idA=f1, pageid=a, ident=5).delete()
    context = {
        "instance": instance,
        "form": form,
        "g": g,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab5A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_cab5']
    BidTbl2.objects.filter(id=idA).update(cab5_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab5sides(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_cab5sides']
    BidTbl2.objects.filter(id=idA).update(cab5sides_id=d, price=1)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab5sidesA(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_cab5sides']
    BidTbl2.objects.filter(id=idA).update(cab5sides_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def drwer5A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_drwer5']
    BidTbl2.objects.filter(id=idA).update(drwer5_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def drwer5(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_drwer5']
    BidTbl2.objects.filter(id=idA).update(drwer5_id=d, price=1)
    a = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    b = ContractInclude.objects.filter(idA=idA, ident=5, pageid=a).delete()
    c = BidTbl2.objects.values_list('custid', flat=True).get(id=idA)
    e = BidTbl2.objects.values_list('conid', flat=True).get(id=idA)
    f = BidTbl2.objects.values_list('drwer5_id', flat=True).get(id=idA)
    g = BidTbl2.objects.values_list('bid_idA', flat=True).get(id=idA)
    h = ContractInclude.objects.create(idA=idA, custid=c, conid=e, bid_idA=g, pageid=a, ident=5, qty=f, name='Drawer',
                                       includeid=0, rmactive=1)
    context = {
        "instance": instance,
        "form": form,
        "h": h,
        "b": b,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletedrwer5(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    b = ContractInclude.objects.filter(idA=idA, ident=5, pageid=a).delete()
    context = {
        "instance": instance,
        "form": form,
        "b": b,
    }
    return render(request, 'wsc/bidpage.html', context)


def c51qty(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_c51qty']
    BidTbl2.objects.filter(id=idA).update(c51qty_id=d)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = CompOption.objects.values_list('price', flat=True).get(ident=51, idA=t1)
    b = int(d)
    c = int(a)
    e = b * c
    f = CompOption.objects.values_list('labor', flat=True).get(ident=51, idA=t1)
    g = int(f)
    h = b * g
    CompOption.objects.filter(ident=51, idA=t1).update(compqty=d, totalprice=e, totallabor=h)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=51, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c51qtyA(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=idA, ident=51).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c52qty(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_c52qty']
    BidTbl2.objects.filter(id=idA).update(c52qty_id=d)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = CompOption.objects.values_list('price', flat=True).get(ident=52, idA=t1)
    b = int(d)
    c = int(a)
    e = b * c
    f = CompOption.objects.values_list('labor', flat=True).get(ident=52, idA=t1)
    g = int(f)
    h = b * g
    CompOption.objects.filter(ident=52, idA=t1).update(compqty=d, totalprice=e, totallabor=h)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=52, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c52qtyA(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=idA, ident=52).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c53qty(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_c53qty']
    BidTbl2.objects.filter(id=idA).update(c53qty_id=d)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = AccOption.objects.values_list('price', flat=True).get(ident=53, idA=t1)
    b = int(d)
    c = int(a)
    e = b * c
    AccOption.objects.filter(ident=53, idA=t1).update(accqty=d, totalprice=e)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=53, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c53qtyA(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    a.filter(bidid=id, ident=53).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c54qty(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_c54qty']
    BidTbl2.objects.filter(id=idA).update(c54qty_id=d)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = AccOption.objects.values_list('price', flat=True).get(ident=54, idA=t1)
    b = int(d)
    c = int(a)
    e = b * c
    AccOption.objects.filter(ident=54, idA=t1).update(accqty=d, totalprice=e)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=54, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c54qtyA(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    a.filter(bidid=id, ident=54).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c55qty(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_c55qty']
    BidTbl2.objects.filter(id=idA).update(c55qty_id=d)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = AccOption.objects.values_list('price', flat=True).get(ident=55, idA=t1)
    b = int(d)
    c = int(a)
    e = b * c
    AccOption.objects.filter(ident=55, idA=t1).update(accqty=d, totalprice=e)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=55, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c55qtyA(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    a.filter(bidid=id, ident=55).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp51A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp51']
    BidTbl2.objects.filter(id=idA).update(comp51_id=d, c51qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp51(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp51']
    BidTbl2.objects.filter(id=idA).update(comp51_id=d, c51qty_id='', price=1)
    e = BidTbl2.objects.all()
    t1 = BidTbl.objects.all()
    f = CompOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=idA)
    f3 = e.values_list('idA', flat=True).get(id=idA)
    g = e.values_list('bid_idA', flat=True).get(id=idA)
    h = e.values_list('custid', flat=True).get(id=idA)
    i = e.values_list('conid', flat=True).get(id=idA)
    j = e.values_list('saleid', flat=True).get(id=idA)
    t2 = t1.values_list('room_id', flat=True).get(id=idA)
    k = Comp.objects.all()
    l = k.values_list('price', flat=True).get(id=d)
    m = k.values_list('labor', flat=True).get(id=d)
    v = CompOption.objects.create(idA=f3, bidid=g, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, comp=d,
                                  ident=51, price=l, labor=m)
    f1 = Comp.objects.all()
    c = Comp.objects.values_list('comp_type', flat=True).get(id=d)
    c1 = CompOption.objects.filter(idA=idA, comp=d).update(compname=c)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.create(idA=idA, custid=h, conid=i, bid_idA=g, pageid=b1, ident=51, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "f2": f2,
        "f1": f1,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp51(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = CompOption.objects.all()
    a.filter(idA=t1, ident=51).delete()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=idA)
    c = ContractInclude.objects.filter(idA=idA, ident=51, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp51A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=idA, ident=51).delete()
    BidTbl2.objects.filter(id=idA).update(comp51_id='', c51qty_id='')
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(idA=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=51, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp52A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp52']
    BidTbl2.objects.filter(id=idA).update(comp52_id=d, c52qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp52(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp52']
    BidTbl2.objects.filter(id=idA).update(comp52_id=d, c52qty_id='', price=1)
    e = BidTbl2.objects.all()
    t1 = BidTbl.objects.all()
    f = CompOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=idA)
    f3 = e.values_list('idA', flat=True).get(id=idA)
    g = e.values_list('bid_idA', flat=True).get(id=idA)
    h = e.values_list('custid', flat=True).get(id=idA)
    i = e.values_list('conid', flat=True).get(id=idA)
    j = e.values_list('saleid', flat=True).get(id=idA)
    t2 = t1.values_list('room_id', flat=True).get(id=idA)
    k = Comp.objects.all()
    l = k.values_list('price', flat=True).get(id=d)
    m = k.values_list('labor', flat=True).get(id=d)
    v = CompOption.objects.create(idA=f3, bidid=g, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, comp=d,
                                  ident=52, price=l, labor=m)
    f1 = Comp.objects.all()
    c = Comp.objects.values_list('comp_type', flat=True).get(id=d)
    c1 = CompOption.objects.filter(idA=idA, comp=d).update(compname=c)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.create(idA=idA, custid=h, conid=i, bid_idA=g, pageid=b1, ident=52, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "f2": f2,
        "f1": f1,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp52(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = CompOption.objects.all()
    a.filter(idA=t1, ident=52).delete()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=idA)
    c = ContractInclude.objects.filter(idA=idA, ident=52, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp52A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=idA, ident=52).delete()
    BidTbl2.objects.filter(id=idA).update(comp52_id='', c52qty_id='')
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(idA=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=52, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp53A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp53']
    BidTbl2.objects.filter(id=idA).update(comp53_id=d, c53qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp53(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp53']
    BidTbl2.objects.filter(id=idA).update(comp53_id=d, c53qty_id='', price=1)
    e = BidTbl2.objects.all()
    t1 = BidTbl.objects.all()
    f = AccOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=idA)
    f3 = e.values_list('idA', flat=True).get(id=idA)
    g = e.values_list('bid_idA', flat=True).get(id=idA)
    h = e.values_list('custid', flat=True).get(id=idA)
    i = e.values_list('conid', flat=True).get(id=idA)
    j = e.values_list('saleid', flat=True).get(id=idA)
    t2 = t1.values_list('room_id', flat=True).get(id=idA)
    k = CabAcc.objects.all()
    f4 = BidTbl2.objects.values_list('bid_idA', flat=True).get(idA=idA)
    l = k.values_list('price', flat=True).get(id=d)
    v = AccOption.objects.create(idA=f3, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, acc=d,
                                 ident=53, price=l)
    c = CabAcc.objects.values_list('cabacc_type', flat=True).get(id=d)
    c1 = AccOption.objects.filter(idA=idA, acc=d).update(accname=c)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.create(idA=idA, custid=h, conid=i, bid_idA=f4, pageid=b1, ident=53, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp53(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = AccOption.objects.all()
    a.filter(idA=t1, ident=53).delete()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=idA)
    c = ContractInclude.objects.filter(idA=idA, ident=53, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp53A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    a.filter(bidid=idA, ident=53).delete()
    BidTbl2.objects.filter(id=idA).update(comp53_id='', c53qty_id='')
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(idA=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=53, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp54A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp54']
    BidTbl2.objects.filter(id=idA).update(comp54_id=d, c54qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp54(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp54']
    BidTbl2.objects.filter(id=idA).update(comp54_id=d, c54qty_id='', price=1)
    e = BidTbl2.objects.all()
    t1 = BidTbl.objects.all()
    f = AccOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=idA)
    f3 = e.values_list('idA', flat=True).get(id=idA)
    g = e.values_list('bid_idA', flat=True).get(id=idA)
    h = e.values_list('custid', flat=True).get(id=idA)
    i = e.values_list('conid', flat=True).get(id=idA)
    j = e.values_list('saleid', flat=True).get(id=idA)
    t2 = t1.values_list('room_id', flat=True).get(id=idA)
    k = CabAcc.objects.all()
    f4 = BidTbl2.objects.values_list('bid_idA', flat=True).get(idA=idA)
    l = k.values_list('price', flat=True).get(id=d)
    v = AccOption.objects.create(idA=f3, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, acc=d,
                                 ident=54, price=l)
    c = CabAcc.objects.values_list('cabacc_type', flat=True).get(id=d)
    c1 = AccOption.objects.filter(idA=idA, acc=d).update(accname=c)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.create(idA=idA, custid=h, conid=i, bid_idA=f4, pageid=b1, ident=54, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp54(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = AccOption.objects.all()
    a.filter(idA=t1, ident=54).delete()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=idA)
    c = ContractInclude.objects.filter(idA=idA, ident=54, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp54A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    a.filter(bidid=idA, ident=54).delete()
    BidTbl2.objects.filter(id=idA).update(comp54_id='', c54qty_id='')
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(idA=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=54, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp55A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp55']
    BidTbl2.objects.filter(id=idA).update(comp55_id=d, c55qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp55(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp55']
    BidTbl2.objects.filter(id=idA).update(comp55_id=d, c55qty_id='', price=1)
    e = BidTbl2.objects.all()
    t1 = BidTbl.objects.all()
    f = AccOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=idA)
    f3 = e.values_list('idA', flat=True).get(id=idA)
    g = e.values_list('bid_idA', flat=True).get(id=idA)
    h = e.values_list('custid', flat=True).get(id=idA)
    i = e.values_list('conid', flat=True).get(id=idA)
    j = e.values_list('saleid', flat=True).get(id=idA)
    t2 = t1.values_list('room_id', flat=True).get(id=idA)
    k = CabAcc.objects.all()
    f4 = BidTbl2.objects.values_list('bid_idA', flat=True).get(idA=idA)
    l = k.values_list('price', flat=True).get(id=d)
    v = AccOption.objects.create(idA=f3, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, acc=d,
                                 ident=55, price=l)
    c = CabAcc.objects.values_list('cabacc_type', flat=True).get(id=d)
    c1 = AccOption.objects.filter(idA=idA, acc=d).update(accname=c)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.create(idA=idA, custid=h, conid=i, bid_idA=f4, pageid=b1, ident=55, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp55(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = AccOption.objects.all()
    a.filter(idA=t1, ident=55).delete()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=idA)
    c = ContractInclude.objects.filter(idA=idA, ident=55, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp55A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    a.filter(bidid=idA, ident=55).delete()
    BidTbl2.objects.filter(id=idA).update(comp55_id='', c55qty_id='')
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(idA=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=55, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab6num(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_cab6num']
    BidTbl2.objects.filter(id=idA).update(cab6num_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab6(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_cab6']
    BidTbl2.objects.filter(id=idA).update(cab6_id=d, price=1)
#    a = BidTbl.objects.values_list('pageid', flat=True).get(id=idA)
#    c = BidTbl.objects.values_list('custid', flat=True).get(id=idA)
#    e = BidTbl.objects.values_list('conid', flat=True).get(id=idA)
#    f = BidTbl2.objects.values_list('cab6_id', flat=True).get(id=idA)
#    f1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=idA)
#    g = ContractInclude.objects.create(idA=idA, custid=c, conid=e, bid_idA=f1, pageid=a, ident=6, qty=f,
#                                       name='Ft. of Cabinets',
#                                       includeid=00, rmactive=1)
    context = {
        "instance": instance,
        "form": form,
#        "g": g,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecab6(request, idA=None):
    instance = get_object_or_404(BidTbl, id=idA)
    form = BidPage(request.POST or None, instance=instance)
    a = BidTbl.objects.values_list('pageid', flat=True).get(id=idA)
    c = BidTbl.objects.values_list('custid', flat=True).get(id=idA)
    e = BidTbl.objects.values_list('conid', flat=True).get(id=idA)
    f1 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=idA)
    g = ContractInclude.objects.filter(idA=idA, custid=c, conid=e, bid_idA=f1, pageid=a, ident=6).delete()
    context = {
        "instance": instance,
        "form": form,
        "g": g,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab6A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_cab6']
    BidTbl2.objects.filter(id=idA).update(cab6_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab6sides(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_cab6sides']
    BidTbl2.objects.filter(id=idA).update(cab6sides_id=d, price=1)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def cab6sidesA(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_cab6sides']
    BidTbl2.objects.filter(id=idA).update(cab6sides_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def drwer6A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_drwer6']
    BidTbl2.objects.filter(id=idA).update(drwer6_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def drwer6(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_drwer6']
    BidTbl2.objects.filter(id=idA).update(drwer6_id=d, price=1)
    a = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    b = ContractInclude.objects.filter(idA=idA, ident=6, pageid=a).delete()
    c = BidTbl2.objects.values_list('custid', flat=True).get(id=idA)
    e = BidTbl2.objects.values_list('conid', flat=True).get(id=idA)
    f = BidTbl2.objects.values_list('drwer6_id', flat=True).get(id=idA)
    g = BidTbl2.objects.values_list('bid_idA', flat=True).get(id=idA)
    h = ContractInclude.objects.create(idA=idA, custid=c, conid=e, bid_idA=g, pageid=a, ident=6, qty=f, name='Drawer',
                                       includeid=0, rmactive=1)
    context = {
        "instance": instance,
        "form": form,
        "h": h,
        "b": b,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletedrwer6(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    b = ContractInclude.objects.filter(idA=idA, ident=6, pageid=a).delete()
    context = {
        "instance": instance,
        "form": form,
        "b": b,
    }
    return render(request, 'wsc/bidpage.html', context)


def c61qty(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_c61qty']
    BidTbl2.objects.filter(id=idA).update(c61qty_id=d)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = CompOption.objects.values_list('price', flat=True).get(ident=61, idA=t1)
    b = int(d)
    c = int(a)
    e = b * c
    f = CompOption.objects.values_list('labor', flat=True).get(ident=61, idA=t1)
    g = int(f)
    h = b * g
    CompOption.objects.filter(ident=61, idA=t1).update(compqty=d, totalprice=e, totallabor=h)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=61, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c61qtyA(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=idA, ident=61).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c62qty(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_c62qty']
    BidTbl2.objects.filter(id=idA).update(c62qty_id=d)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = CompOption.objects.values_list('price', flat=True).get(ident=62, idA=t1)
    b = int(d)
    c = int(a)
    e = b * c
    f = CompOption.objects.values_list('labor', flat=True).get(ident=62, idA=t1)
    g = int(f)
    h = b * g
    CompOption.objects.filter(ident=62, idA=t1).update(compqty=d, totalprice=e, totallabor=h)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=62, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c62qtyA(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=idA, ident=62).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c63qty(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_c63qty']
    BidTbl2.objects.filter(id=idA).update(c63qty_id=d)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = AccOption.objects.values_list('price', flat=True).get(ident=63, idA=t1)
    b = int(d)
    c = int(a)
    e = b * c
    AccOption.objects.filter(ident=63, idA=t1).update(accqty=d, totalprice=e)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=63, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c63qtyA(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    a.filter(bidid=id, ident=63).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c64qty(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_c64qty']
    BidTbl2.objects.filter(id=idA).update(c64qty_id=d)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = AccOption.objects.values_list('price', flat=True).get(ident=64, idA=t1)
    b = int(d)
    c = int(a)
    e = b * c
    AccOption.objects.filter(ident=64, idA=t1).update(accqty=d, totalprice=e)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=64, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c64qtyA(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    a.filter(bidid=id, ident=64).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def c65qty(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_c65qty']
    BidTbl2.objects.filter(id=idA).update(c65qty_id=d)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = AccOption.objects.values_list('price', flat=True).get(ident=65, idA=t1)
    b = int(d)
    c = int(a)
    e = b * c
    AccOption.objects.filter(ident=65, idA=t1).update(accqty=d, totalprice=e)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=65, pageid=b1).update(qty=d)
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def c65qtyA(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    a.filter(bidid=id, ident=65).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp61A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp61']
    BidTbl2.objects.filter(id=idA).update(comp61_id=d, c61qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp61(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp61']
    BidTbl2.objects.filter(id=idA).update(comp61_id=d, c61qty_id='', price=1)
    e = BidTbl2.objects.all()
    t1 = BidTbl.objects.all()
    f = CompOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=idA)
    f3 = e.values_list('idA', flat=True).get(id=idA)
    g = e.values_list('bid_idA', flat=True).get(id=idA)
    h = e.values_list('custid', flat=True).get(id=idA)
    i = e.values_list('conid', flat=True).get(id=idA)
    j = e.values_list('saleid', flat=True).get(id=idA)
    t2 = t1.values_list('room_id', flat=True).get(id=idA)
    k = Comp.objects.all()
    l = k.values_list('price', flat=True).get(id=d)
    m = k.values_list('labor', flat=True).get(id=d)
    v = CompOption.objects.create(idA=f3, bidid=g, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, comp=d,
                                  ident=61, price=l, labor=m)
    f1 = Comp.objects.all()
    c = Comp.objects.values_list('comp_type', flat=True).get(id=d)
    c1 = CompOption.objects.filter(idA=idA, comp=d).update(compname=c)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.create(idA=idA, custid=h, conid=i, bid_idA=g, pageid=b1, ident=61, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "f2": f2,
        "f1": f1,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp61(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = CompOption.objects.all()
    a.filter(idA=t1, ident=61).delete()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=idA)
    c = ContractInclude.objects.filter(idA=idA, ident=61, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp61A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=idA, ident=61).delete()
    BidTbl2.objects.filter(id=idA).update(comp61_id='', c61qty_id='')
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(idA=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=61, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp62A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp62']
    BidTbl2.objects.filter(id=idA).update(comp62_id=d, c62qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp62(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp62']
    BidTbl2.objects.filter(id=idA).update(comp62_id=d, c62qty_id='', price=1)
    e = BidTbl2.objects.all()
    t1 = BidTbl.objects.all()
    f = CompOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=idA)
    f3 = e.values_list('idA', flat=True).get(id=idA)
    g = e.values_list('bid_idA', flat=True).get(id=idA)
    h = e.values_list('custid', flat=True).get(id=idA)
    i = e.values_list('conid', flat=True).get(id=idA)
    j = e.values_list('saleid', flat=True).get(id=idA)
    t2 = t1.values_list('room_id', flat=True).get(id=idA)
    k = Comp.objects.all()
    l = k.values_list('price', flat=True).get(id=d)
    m = k.values_list('labor', flat=True).get(id=d)
    v = CompOption.objects.create(idA=f3, bidid=g, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, comp=d,
                                  ident=62, price=l, labor=m)
    f1 = Comp.objects.all()
    c = Comp.objects.values_list('comp_type', flat=True).get(id=d)
    c1 = CompOption.objects.filter(idA=idA, comp=d).update(compname=c)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.create(idA=idA, custid=h, conid=i, bid_idA=g, pageid=b1, ident=62, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "f2": f2,
        "f1": f1,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp62(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = CompOption.objects.all()
    a.filter(idA=t1, ident=62).delete()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=idA)
    c = ContractInclude.objects.filter(idA=idA, ident=62, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp62A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = CompOption.objects.all()
    a.filter(bidid=idA, ident=62).delete()
    BidTbl2.objects.filter(id=idA).update(comp62_id='', c62qty_id='')
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(idA=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=62, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp63A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp63']
    BidTbl2.objects.filter(id=idA).update(comp63_id=d, c63qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp63(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp63']
    BidTbl2.objects.filter(id=idA).update(comp63_id=d, c63qty_id='', price=1)
    e = BidTbl2.objects.all()
    t1 = BidTbl.objects.all()
    f = AccOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=idA)
    f3 = e.values_list('idA', flat=True).get(id=idA)
    g = e.values_list('bid_idA', flat=True).get(id=idA)
    h = e.values_list('custid', flat=True).get(id=idA)
    i = e.values_list('conid', flat=True).get(id=idA)
    j = e.values_list('saleid', flat=True).get(id=idA)
    t2 = t1.values_list('room_id', flat=True).get(id=idA)
    k = CabAcc.objects.all()
    f4 = BidTbl2.objects.values_list('bid_idA', flat=True).get(idA=idA)
    l = k.values_list('price', flat=True).get(id=d)
    v = AccOption.objects.create(idA=f3, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, acc=d,
                                 ident=63, price=l)
    c = CabAcc.objects.values_list('cabacc_type', flat=True).get(id=d)
    c1 = AccOption.objects.filter(idA=idA, acc=d).update(accname=c)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.create(idA=idA, custid=h, conid=i, bid_idA=f4, pageid=b1, ident=63, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp63(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = AccOption.objects.all()
    a.filter(idA=t1, ident=63).delete()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=idA)
    c = ContractInclude.objects.filter(idA=idA, ident=63, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp63A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    a.filter(bidid=idA, ident=63).delete()
    BidTbl2.objects.filter(id=idA).update(comp63_id='', c63qty_id='')
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(idA=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=63, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp64A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp64']
    BidTbl2.objects.filter(id=idA).update(comp64_id=d, c64qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp64(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp64']
    BidTbl2.objects.filter(id=idA).update(comp64_id=d, c64qty_id='', price=1)
    e = BidTbl2.objects.all()
    t1 = BidTbl.objects.all()
    f = AccOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=idA)
    f3 = e.values_list('idA', flat=True).get(id=idA)
    g = e.values_list('bid_idA', flat=True).get(id=idA)
    h = e.values_list('custid', flat=True).get(id=idA)
    i = e.values_list('conid', flat=True).get(id=idA)
    j = e.values_list('saleid', flat=True).get(id=idA)
    t2 = t1.values_list('room_id', flat=True).get(id=idA)
    k = CabAcc.objects.all()
    f4 = BidTbl2.objects.values_list('bid_idA', flat=True).get(idA=idA)
    l = k.values_list('price', flat=True).get(id=d)
    v = AccOption.objects.create(idA=f3, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, acc=d,
                                 ident=64, price=l)
    c = CabAcc.objects.values_list('cabacc_type', flat=True).get(id=d)
    c1 = AccOption.objects.filter(idA=idA, acc=d).update(accname=c)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.create(idA=idA, custid=h, conid=i, bid_idA=f4, pageid=b1, ident=64, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp64(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = AccOption.objects.all()
    a.filter(idA=t1, ident=64).delete()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=idA)
    c = ContractInclude.objects.filter(idA=idA, ident=64, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp64A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    a.filter(bidid=idA, ident=64).delete()
    BidTbl2.objects.filter(id=idA).update(comp64_id='', c64qty_id='')
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(idA=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=64, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp65A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp65']
    BidTbl2.objects.filter(id=idA).update(comp65_id=d, c65qty_id='')

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpage.html', context)


def comp65(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    d = request.POST['id_comp65']
    BidTbl2.objects.filter(id=idA).update(comp65_id=d, c65qty_id='', price=1)
    e = BidTbl2.objects.all()
    t1 = BidTbl.objects.all()
    f = AccOption.objects.all()
    f2 = e.values_list('pageid', flat=True).get(id=idA)
    f3 = e.values_list('idA', flat=True).get(id=idA)
    g = e.values_list('bid_idA', flat=True).get(id=idA)
    h = e.values_list('custid', flat=True).get(id=idA)
    i = e.values_list('conid', flat=True).get(id=idA)
    j = e.values_list('saleid', flat=True).get(id=idA)
    t2 = t1.values_list('room_id', flat=True).get(id=idA)
    k = CabAcc.objects.all()
    f4 = BidTbl2.objects.values_list('bid_idA', flat=True).get(idA=idA)
    l = k.values_list('price', flat=True).get(id=d)
    v = AccOption.objects.create(idA=f3, pageid=f2, bid_idA=g, custid=h, conid=i, saleid=j, roomid=t2, acc=d,
                                 ident=65, price=l)
    c = CabAcc.objects.values_list('cabacc_type', flat=True).get(id=d)
    c1 = AccOption.objects.filter(idA=idA, acc=d).update(accname=c)
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(id=idA)
    g1 = ContractInclude.objects.create(idA=idA, custid=h, conid=i, bid_idA=f4, pageid=b1, ident=65, name=c, includeid=d,
                                        rmactive=1)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "c1": c1,
        "v": v,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp65(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    t1 = BidTbl2.objects.values_list('idA', flat=True).get(id=idA)
    a = AccOption.objects.all()
    a.filter(idA=t1, ident=65).delete()
    b = BidTbl.objects.values_list('pageid', flat=True).get(id=idA)
    c = ContractInclude.objects.filter(idA=idA, ident=65, pageid=b).delete()
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'wsc/bidpage.html', context)


def deletecomp65A(request, idA=None):
    instance = get_object_or_404(BidTbl2, id=idA)
    form = BidPage2(request.POST or None, instance=instance)
    a = AccOption.objects.all()
    a.filter(bidid=idA, ident=65).delete()
    BidTbl2.objects.filter(id=idA).update(comp65_id='', c65qty_id='')
    b1 = BidTbl2.objects.values_list('pageid', flat=True).get(idA=idA)
    g1 = ContractInclude.objects.filter(idA=idA, ident=65, pageid=b1).delete()
    context = {
        "instance": instance,
        "form": form,
        "g1": g1,
    }
    return render(request, 'wsc/bidpage.html', context)


def newbidpage(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = BidTbl.objects.all()
    b = BidTbl2.objects.all()
    bb = a.values_list('bid_idA', flat=True).filter(id=id).distinct()
    i = BidTbl.objects.create(bid_idA=bb)
    j = BidTbl2.objects.create(bid_idA=bb)

    c = a.values_list('pageid', flat=True).get(id=id)
    cc = a.values_list('maxnum', flat=True).get(id=id)
    d = a.values_list('custid', flat=True).get(id=id)
    e = a.values_list('conid', flat=True).get(id=id)
    f = a.values_list('saleid', flat=True).get(id=id)
    g = a.values_list('custlastname', flat=True).get(id=id)
    h = a.values_list('custadd1', flat=True).get(id=id)
    hh = a.values_list('room_id', flat=True).get(id=id)
    m = BidTbl.objects.values_list('id', flat=True).last()

    n = BidTbl2.objects.values_list('id', flat=True).last()
    BidTbl.objects.filter(id=id).update(max=0)
    BidTbl.objects.filter(id=m).update(pageid=cc + 1, custid=d, conid=e, saleid=f, custlastname=g, custadd1=h,
                                       room_id=hh
                                       , max=1, maxnum=c + 1, price=1, rmactive=1)
    BidTbl2.objects.filter(id=n).update(idA=m, pageid=c + 1, custid=d, conid=e, saleid=f)
    time.sleep(.5)
    t1 = a.values_list('maxnum', flat=True).get(id=m)
    t2 = a.values_list('bid_idA', flat=True).get(id=m)

    t3 = BidTbl.objects.filter(bid_idA=t2).update(maxnum=t1)
    instance6 = BidTbl.objects.order_by('id').last()
    context = {
        "instance": instance,
        "form": form,
        "i": i,
        "j": j,
        "b": b,
        "t3": t3,

    }
    return redirect(instance6.get_absolute11_url(), context)


def previouspage(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    a = BidTbl.objects.all()
    b = a.values_list('pageid', flat=True).get(id=id)
    c = a.values_list('bid_idA', flat=True).get(id=id)
    d = b - 1
    instance6 = BidTbl.objects.order_by('id').get(pageid=d, bid_idA=c)
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance6.get_absolute11_url(), context)


def viewnext(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPage(request.POST or None, instance=instance)
    form2 = BidPage2(request.POST or None, instance=instance)
    a = BidTbl.objects.all()
    b = a.values_list('pageid', flat=True).get(id=id)
    c = a.values_list('bid_idA', flat=True).get(id=id)
    d = b + 1
    instance6 = BidTbl.objects.order_by('id').get(pageid=d, bid_idA=c)
    context = {
        "instance": instance,
        "form": form,
        "form2": form2,
    }
    return redirect(instance6.get_absolute11_url(), context)


def changermnum(request, bid_idA=None):
    instance = get_object_or_404(BidTbl, bid_idA=bid_idA)
    form = AddNewRm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute14_url(), context2)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/changermnum.html', context)


def updatetotalrmcost(request, bid_idA=None):
    instance = TotalRoomCost.objects.get(bid_idA=bid_idA)
    instance2 = TotalRoomCost.objects.values_list('bid_idA', flat=True).get(bid_idA=bid_idA)
    form = TotalRmCost(request.POST or None, instance=instance)
    AccOptionTotal.objects.filter(bid_idA=bid_idA).delete()
    CompOptionTotal.objects.filter(bid_idA=bid_idA).delete()
    a = BidTbl.objects.all()
    b = BidTbl2.objects.all()
    aa = Pricing.objects.all()
    cc = Comp.objects.all()
    dd = CabAcc.objects.all()
    ee = CustomerInfo.objects.all()
    ff = TotalRoomCost.objects.values_list('custid', flat=True).get(bid_idA=bid_idA)
    gg = ee.values_list('prodqueue_id', flat=True).get(custid=ff) or 0
    hh = TotalRoomCost.objects.values_list('totalperc', flat=True).get(bid_idA=bid_idA) or 0
    c = a.filter(bid_idA=instance2).aggregate(Sum('cab1_id')).get('cab1_id__sum') or 0
    d = a.filter(bid_idA=instance2).aggregate(Sum('cab2_id')).get('cab2_id__sum') or 0
    e = a.filter(bid_idA=instance2).aggregate(Sum('cab3_id')).get('cab3_id__sum') or 0
    f = b.filter(bid_idA=instance2).aggregate(Sum('cab4_id')).get('cab4_id__sum') or 0
    g = b.filter(bid_idA=instance2).aggregate(Sum('cab5_id')).get('cab5_id__sum') or 0
    h = b.filter(bid_idA=instance2).aggregate(Sum('cab6_id')).get('cab6_id__sum') or 0
    ii = c + d + e + f + g + h  ## 2
    j4 = aa.values_list('cabinet', flat=True).last()  ## 200
    k4 = j4 * gg  ### Cabinet Price * Prodqueue = Prod. Increase
    l4 = j4 + k4  ### Cabinet Price + Prodqueue
    m4 = l4 * ii  ### Cabinet Price Total
    n4 = j4 * ii  ### Total Numbers of Cabinets * Cabinet Price ###  400
    o4 = n4 * hh
    p4 = o4 + n4  ### Cabinet Price + Total Percentage from TotalRoomCost Page ###
    c1 = a.filter(bid_idA=instance2).aggregate(Sum('cab1sides_id')).get('cab1sides_id__sum') or 0
    d1 = a.filter(bid_idA=instance2).aggregate(Sum('cab2sides_id')).get('cab2sides_id__sum') or 0
    e1 = a.filter(bid_idA=instance2).aggregate(Sum('cab3sides_id')).get('cab3sides_id__sum') or 0
    f1 = b.filter(bid_idA=instance2).aggregate(Sum('cab4sides_id')).get('cab4sides_id__sum') or 0
    g1 = b.filter(bid_idA=instance2).aggregate(Sum('cab5sides_id')).get('cab5sides_id__sum') or 0
    h1 = b.filter(bid_idA=instance2).aggregate(Sum('cab6sides_id')).get('cab6sides_id__sum') or 0
    i1 = c1 + d1 + e1 + f1 + g1 + h1
    j1 = aa.values_list('sides', flat=True).last()
    o5 = j1 * gg
    p5 = j1 + o5
    k5 = i1 * p5
    l5 = i1 * j1
    m5 = l5 * hh
    n5 = l5 + m5
    c2 = a.filter(bid_idA=instance2).aggregate(Sum('drwer1_id')).get('drwer1_id__sum') or 0
    d2 = a.filter(bid_idA=instance2).aggregate(Sum('drwer2_id')).get('drwer2_id__sum') or 0
    e2 = a.filter(bid_idA=instance2).aggregate(Sum('drwer3_id')).get('drwer3_id__sum') or 0
    f2 = b.filter(bid_idA=instance2).aggregate(Sum('drwer4_id')).get('drwer4_id__sum') or 0
    g2 = b.filter(bid_idA=instance2).aggregate(Sum('drwer5_id')).get('drwer5_id__sum') or 0
    h2 = b.filter(bid_idA=instance2).aggregate(Sum('drwer6_id')).get('drwer6_id__sum') or 0
    i2 = c2 + d2 + e2 + f2 + g2 + h2
    j2 = aa.values_list('drawer', flat=True).last()
    o6 = j2 * gg
    p6 = j2 + o6
    k6 = i2 * p6
    l6 = j2 * i2
    data = CompOption.objects.filter(bid_idA=bid_idA).values('comp', 'bid_idA', 'custid', 'conid', ) \
        .order_by('comp').annotate(compqty=Sum('compqty'), price=Sum('price'))
    w = CompOptionTotal.objects.bulk_create([CompOptionTotal(**q) for q in data])
    x = CompOptionTotal.objects.filter(bid_idA=bid_idA).values_list('compqty', 'price')
    y = sum(t[0] * t[1] for t in x)
    o9 = y * gg
    p9 = y + o9
    q9 = y * hh
    r9 = y + q9
    data1 = AccOption.objects.filter(bid_idA=bid_idA).values('acc', 'bid_idA', 'custid', 'conid') \
        .order_by('acc').annotate(total_qty=Sum('accqty'), price=Sum('price'))
    ww = AccOptionTotal.objects.bulk_create([AccOptionTotal(**q) for q in data1])
    xx = AccOptionTotal.objects.filter(bid_idA=bid_idA).values_list('total_qty', 'price')
    yy = sum(t[0] * t[1] for t in xx)
    o7 = yy * gg
    p7 = yy + o7
    #   z = BidTbl.objects.values_list('room_id', flat=True).distinct().get(bid_idA=bid_idA)
    objs = BidTbl.objects.filter(bid_idA=instance2)
    objs.update(price=0)
    objs2 = BidTbl2.objects.filter(bid_idA=instance2)
    objs2.update(price=0)
    m = TotalRoomCost.objects.values_list('optionnum', flat=True).get(bid_idA=bid_idA) or 0
    m8 = TotalRoomCost.objects.values_list('cabaccrmtotal', flat=True).get(bid_idA=bid_idA) or 0
    p8 = TotalRoomCost.objects.values_list('cabacccustom', flat=True).get(bid_idA=bid_idA) or 0
    r8 = m8 + p8
    p = TotalRoomCost.objects.values_list('custcabtotal', flat=True).get(bid_idA=bid_idA) or 0
    q = TotalRoomCost.objects.values_list('custsidetotal', flat=True).get(bid_idA=bid_idA) or 0
    r = TotalRoomCost.objects.values_list('drawertotal', flat=True).get(bid_idA=bid_idA) or 0
    s = TotalRoomCost.objects.values_list('optionnum', flat=True).get(bid_idA=bid_idA) or 0
    t = TotalRoomCost.objects.values_list('cabacctotal', flat=True).get(bid_idA=bid_idA) or 0

    www = TotalRoomCost.objects.values_list('woodspecies_id', flat=True).get(bid_idA=bid_idA) or 2
    xxx = TotalRoomCost.objects.values_list('doorstyle_id', flat=True).get(bid_idA=bid_idA) or 2
    yyy = TotalRoomCost.objects.values_list('finishcolor_id', flat=True).get(bid_idA=bid_idA) or 2
    zzz = TotalRoomCost.objects.values_list('finishoption1_id', flat=True).get(bid_idA=bid_idA) or 1
    TotalRoomCost.objects.filter(bid_idA=instance2).update(cabnumtotal=ii, cabinet=l4, cabtotalprice=m4, cabsidenum=i1,
                                                           cabsidecost=p5, cabsidetotal=k5, drawernum=i2,
                                                           drawercost=p6, drawertotal=k6, cabaccrmtotal=y,
                                                           optionnum=yy, woodspecies_id=www, doorstyle_id=xxx,
                                                           finishcolor_id=yyy, finishoption1_id=zzz)
    totals = p + q + r + s + t
    Totals.objects.filter(bid_idA=instance2).update(rmcost=totals)
    b11 = Totals.objects.values_list('totalincrease', flat=True).get(bid_idA=bid_idA)
    b12 = Totals.objects.values_list('rmcost', flat=True).get(bid_idA=bid_idA)
    b13 = b11 + b12
    ###b14 = TotalRoomCost.objects.values_list('prodqueuetotal', flat=True).get(bid_idA=bid_idA)
    b20 = Totals.objects.values_list('rmcost', flat=True).get(bid_idA=bid_idA)
    b21 = Totals.objects.values_list('increase', flat=True).get(bid_idA=bid_idA)
    b22 = b20 * b21
    Totals.objects.filter(bid_idA=instance2).update(totalrmcost=b13)
    TotalRoomCost.objects.filter(bid_idA=bid_idA).update(totalrmcost=b12)
    TotalRoomCost.objects.filter(bid_idA=bid_idA).update(prodqueuetotal=b22)
    b23 = b12 + b22
    CurrentRm.objects.filter(bid_idA=instance2).update(rmcost=b23)
    TotalRoomCost.objects.filter(bid_idA=bid_idA).update(rmgrandtotal=b23)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute13_url())
    context = {
        "instance": instance,
        "form": form,
        "cc": cc,
        "dd": dd,
        "w": w,
        "ww": ww,
    }
    return redirect(instance.get_absolute13_url(), context)


def totalrmcost(request, bid_idA=None):
    instance = TotalRoomCost.objects.get(bid_idA=bid_idA)
    instance2 = TotalRoomCost.objects.values_list('bid_idA', flat=True).get(bid_idA=bid_idA)
    form = TotalRmCost(request.POST or None, instance=instance)
    # Labor.objects.filter(bid_idA=bid_idA).delete()
    AccOptionTotal.objects.filter(bid_idA=bid_idA).delete()
    CompOptionTotal.objects.filter(bid_idA=bid_idA).delete()
    Labor.objects.filter(bid_idA=bid_idA).delete()
    Cabinet.objects.filter(bid_idA=bid_idA).delete()
    a = BidTbl.objects.all()
    b = BidTbl2.objects.all()
    aa = Pricing.objects.all()
    cc = Comp.objects.all()
    dd = CabAcc.objects.all()
    ee = CustomerInfo.objects.all()
    ff = TotalRoomCost.objects.values_list('custid', flat=True).get(bid_idA=bid_idA)
    ffaa = TotalRoomCost.objects.values_list('conid', flat=True).get(bid_idA=bid_idA)
    ffab = TotalRoomCost.objects.values_list('room_id', flat=True).get(bid_idA=bid_idA)
    gg = ee.values_list('prodqueue_id', flat=True).get(custid=ff) or 0
    hh = TotalRoomCost.objects.values_list('totalperc', flat=True).get(bid_idA=bid_idA) or 0
    c = a.filter(bid_idA=instance2).aggregate(Sum('cab1_id')).get('cab1_id__sum') or 0
    d = a.filter(bid_idA=instance2).aggregate(Sum('cab2_id')).get('cab2_id__sum') or 0
    e = a.filter(bid_idA=instance2).aggregate(Sum('cab3_id')).get('cab3_id__sum') or 0
    f = b.filter(bid_idA=instance2).aggregate(Sum('cab4_id')).get('cab4_id__sum') or 0
    g = b.filter(bid_idA=instance2).aggregate(Sum('cab5_id')).get('cab5_id__sum') or 0
    h = b.filter(bid_idA=instance2).aggregate(Sum('cab6_id')).get('cab6_id__sum') or 0
    ii = c + d + e + f + g + h  ## 2
    j4 = aa.values_list('cabinet', flat=True).last()  ## 200
    j4a = aa.values_list('cab_labor', flat=True).last()  ## 300
    k4 = j4 * gg  ### Cabinet Price * Prodqueue = Prod. Increase
    l4 = j4 + k4  ### Cabinet Price + Prodqueue
    m4 = l4 * ii  ### Cabinet Price Total
    n4 = j4 * ii  ### Total Numbers of Cabinets * Cabinet Price ###  400
#    o4 = n4 * hh
#    p4 = o4 + n4  ### Cabinet Price + Total Percentage from TotalRoomCost Page ###
    Cabinet.objects.create(bid_idA=bid_idA, custid=ff, conid=ffaa, cabqty=ii, cablabor=j4a)
    c1 = a.filter(bid_idA=instance2).aggregate(Sum('cab1sides_id')).get('cab1sides_id__sum') or 0
    d1 = a.filter(bid_idA=instance2).aggregate(Sum('cab2sides_id')).get('cab2sides_id__sum') or 0
    e1 = a.filter(bid_idA=instance2).aggregate(Sum('cab3sides_id')).get('cab3sides_id__sum') or 0
    f1 = b.filter(bid_idA=instance2).aggregate(Sum('cab4sides_id')).get('cab4sides_id__sum') or 0
    g1 = b.filter(bid_idA=instance2).aggregate(Sum('cab5sides_id')).get('cab5sides_id__sum') or 0
    h1 = b.filter(bid_idA=instance2).aggregate(Sum('cab6sides_id')).get('cab6sides_id__sum') or 0
    i1 = c1 + d1 + e1 + f1 + g1 + h1
    j1 = aa.values_list('sides', flat=True).last()
    o5 = j1 * gg
    p5t = j1 + o5
    k5 = i1 * p5t
    l5 = i1 * j1
#    m5 = l5 * hh
#    n5 = l5 + m5
    c2 = a.filter(bid_idA=instance2).aggregate(Sum('drwer1_id')).get('drwer1_id__sum') or 0
    d2 = a.filter(bid_idA=instance2).aggregate(Sum('drwer2_id')).get('drwer2_id__sum') or 0
    e2 = a.filter(bid_idA=instance2).aggregate(Sum('drwer3_id')).get('drwer3_id__sum') or 0
    f2 = b.filter(bid_idA=instance2).aggregate(Sum('drwer4_id')).get('drwer4_id__sum') or 0
    g2 = b.filter(bid_idA=instance2).aggregate(Sum('drwer5_id')).get('drwer5_id__sum') or 0
    h2 = b.filter(bid_idA=instance2).aggregate(Sum('drwer6_id')).get('drwer6_id__sum') or 0
    i2 = c2 + d2 + e2 + f2 + g2 + h2
    j2 = aa.values_list('drawer', flat=True).last()
    o6 = j2 * gg
    p6t = j2 + o6
    k6 = i2 * p6t
#    l6 = j2 * i2
    data = CompOption.objects.filter(bid_idA=bid_idA).values('comp', 'bid_idA', 'custid', 'conid', 'roomid', 'compname',
                                                             'labor') \
        .order_by('comp').annotate(compqty=Sum('compqty'), totalprice=Sum('totalprice'), totallabor=Sum('totallabor'))
    w = CompOptionTotal.objects.bulk_create([CompOptionTotal(**q) for q in data])
    x = CompOptionTotal.objects.filter(bid_idA=bid_idA).aggregate(Sum('totalprice')).get('totalprice__sum') or 0
    Totals.objects.filter(bid_idA=instance2).update(cabaccrmtotal=x)
    p4 = Totals.objects.values_list('cabaccrmtotal', flat=True).get(bid_idA=instance2)
    p5 = p4 * gg
    Totals.objects.filter(bid_idA=instance2).update(cabaccrmtotalincrease=p5)
    p6 = p4 + p5
    Totals.objects.filter(bid_idA=instance2).update(cabaccrmtotaltotal=p6)
    y = CompOptionTotal.objects.filter(bid_idA=bid_idA).aggregate(Sum('totallabor')).get('totallabor__sum') or 0

    a1 = AccOption.objects.values_list('bid_idA', flat=True).filter(bid_idA=bid_idA).first()
    data1 = AccOption.objects.filter(bid_idA=a1).values('acc', 'bid_idA', 'custid', 'conid') \
        .order_by('acc').annotate(total_qty=Sum('accqty'), totalprice=Sum('totalprice'))
    ww = AccOptionTotal.objects.bulk_create([AccOptionTotal(**q) for q in data1])
    yy = AccOptionTotal.objects.filter(bid_idA=bid_idA).aggregate(Sum('totalprice')).get('totalprice__sum') or 0
    Totals.objects.filter(bid_idA=instance2).update(optionnum=yy)
    p1 = Totals.objects.values_list('optionnum', flat=True).get(bid_idA=instance2)
    p2 = p1 * gg
    Totals.objects.filter(bid_idA=instance2).update(optionnumincrease=p2)
    p3 = p1 + p2
    Totals.objects.filter(bid_idA=instance2).update(optionnumtotal=p3)
    objs = BidTbl.objects.filter(bid_idA=instance2)
    objs.update(price=0)
    objs2 = BidTbl2.objects.filter(bid_idA=instance2)
    objs2.update(price=0)
#    m8 = TotalRoomCost.objects.values_list('cabaccrmtotal', flat=True).get(bid_idA=bid_idA) or 0
#    p8 = TotalRoomCost.objects.values_list('cabacccustom', flat=True).get(bid_idA=bid_idA) or 0
#    r8 = m8 + p8
    p = TotalRoomCost.objects.values_list('custcabtotal', flat=True).get(bid_idA=bid_idA) or 0
    q = TotalRoomCost.objects.values_list('custsidetotal', flat=True).get(bid_idA=bid_idA) or 0
    r = TotalRoomCost.objects.values_list('drawertotal', flat=True).get(bid_idA=bid_idA) or 0
    s = TotalRoomCost.objects.values_list('optionnum', flat=True).get(bid_idA=bid_idA) or 0
    t = TotalRoomCost.objects.values_list('cabacctotal', flat=True).get(bid_idA=bid_idA) or 0
    t9 = TotalRoomCost.objects.values_list('room_id', flat=True).get(bid_idA=bid_idA) or 2
    t10 = RoomType.objects.values_list('room_type', flat=True).get(id=t9)
    www = TotalRoomCost.objects.values_list('woodspecies_id', flat=True).get(
        bid_idA=bid_idA) or WoodSpecies.objects.values_list('id', flat=True).first()
    t2 = WoodSpecies.objects.values_list('woodspecies', flat=True).get(id=www)
    xxx = TotalRoomCost.objects.values_list('doorstyle_id', flat=True).get(
        bid_idA=bid_idA) or DoorStyle.objects.values_list('id', flat=True).first()
    t4 = DoorStyle.objects.values_list('doorstyle', flat=True).get(id=xxx)
    yyy = TotalRoomCost.objects.values_list('finishcolor_id', flat=True).get(
        bid_idA=bid_idA) or FinishColor.objects.values_list('id', flat=True).first()
    t6 = FinishColor.objects.values_list('finishcolor', flat=True).get(id=yyy)
    zzz = TotalRoomCost.objects.values_list('finishoption1_id', flat=True).get(
        bid_idA=bid_idA) or FinishOption.objects.values_list('id', flat=True).first()
    t8 = FinishOption.objects.values_list('finishoption', flat=True).get(id=zzz)
    zzz1 = TotalRoomCost.objects.values_list('finishoption2_id', flat=True).get(
        bid_idA=bid_idA) or FinishOption.objects.values_list('id', flat=True).first()
    t81 = FinishOption.objects.values_list('finishoption', flat=True).get(id=zzz1)

    totals = p + q + r + s + t

    b30 = CustomerInfo.objects.values_list('prodqueue_id', flat=True).get(id=ff)
    b33 = int(totals)
    b31 = b33 * b30
#    Totals.objects.filter(bid_idA=instance2).update(totalincrease=b31)
    b32 = b33 + b31
#    b34 = Totals.objects.filter(bid_idA=instance2).update(totalrmcost=b32)
    CurrentRm.objects.filter(bid_idA=instance2).update(rmcost=b32)

    TotalRoomCost.objects.filter(bid_idA=instance2).update(cabnumtotal=ii, cabinet=l4, cabtotalprice=m4, cabsidenum=i1,
                                                           cabsidecost=p5t, cabsidetotal=k5, drawernum=i2,
                                                           drawercost=p6t, drawertotal=k6, cabaccrmtotal=p6, optionnum=p3,
                                                           woodspecies_id=www, doorstyle_id=xxx,
                                                           finishcolor_id=yyy, finishoption1_id=zzz,
                                                           finishoption2_id=zzz1,
                                                           totalrmcost=b32, prodqueuetotal=b31,
                                                           totallabor=y, rmactive=1, wood=t2, door=t4, fncolor=t6,
                                                           fnoption=t8, fnoption2=t81, rmname=t10)
    z3 = TotalRoomCost.objects.values_list('room_id', flat=True).get(bid_idA=bid_idA)
    z1a = Cabinet.objects.values_list('cabqty', flat=True).get(bid_idA=bid_idA) or 0
    z1b = Cabinet.objects.values_list('cablabor', flat=True).get(bid_idA=bid_idA) or 0

    z1c = z1a * z1b
    Cabinet.objects.filter(bid_idA=bid_idA).update(totalcablabor=z1c, roomid=ffab)
    Labor.objects.create(custid=ff, conid=ffaa, bid_idA=instance2, room=z3, labor=y, rmactive=1)
    z1 = Pricing.objects.values_list('cab_labor', flat=True).last()
    z2 = ii * z1
    Labor.objects.create(custid=ff, conid=ffaa, bid_idA=instance2, room=z3, labor=z2, rmactive=1)
#    Totals.objects.filter(bid_idA=instance2).update(baseprice=totals)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute13_url())
    context = {
        "instance": instance,
        "form": form,
        "cc": cc,
        "dd": dd,
        "w": w,
        "ww": ww,
 #       "b34": b34,
    }
    return render(request, 'wsc/totalrmcost.html', context)


def totalrmcost2(request, bid_idA=None):
    instance = TotalRoomCost.objects.get(bid_idA=bid_idA)
    instance2 = TotalRoomCost.objects.values_list('bid_idA', flat=True).get(bid_idA=bid_idA)
    form = TotalRmCost(request.POST or None, instance=instance)
    aa = Pricing.objects.all()
    ee = CustomerInfo.objects.all()
    ff = TotalRoomCost.objects.values_list('custid', flat=True).get(bid_idA=bid_idA)
    gg = ee.values_list('prodqueue_id', flat=True).get(custid=ff) or 0
    ii = TotalRoomCost.objects.values_list('cabnumtotal', flat=True).get(bid_idA=bid_idA)
    j4 = aa.values_list('cabinet', flat=True).last()  ## 200
    k4 = j4 * gg  ### Cabinet Price * Prodqueue = Prod. Increase
    l4 = j4 + k4  ### Cabinet Price + Prodqueue
    m4 = l4 * ii  ### Cabinet Price Total
    t1 = TotalRoomCost.objects.values_list('custcabcost', flat=True).get(bid_idA=bid_idA)
    t2 = m4 + t1
    i1 = TotalRoomCost.objects.values_list('cabsidenum', flat=True).get(bid_idA=bid_idA)
    j1 = aa.values_list('sides', flat=True).last()
    o5 = j1 * gg
    p5t = j1 + o5
    k5 = i1 * p5t
    t5 = TotalRoomCost.objects.values_list('custsidecost', flat=True).get(bid_idA=bid_idA)
    l5 = k5 + t5

    m5 = TotalRoomCost.objects.values_list('drawernum', flat=True).get(bid_idA=bid_idA)
    m5a = aa.values_list('drawer', flat=True).last()
    m6a = m5a * gg
    m6b = m5a + m6a
    m7 = m5 * m6b
    m6 = TotalRoomCost.objects.values_list('drawercost', flat=True).get(bid_idA=bid_idA)
    m8 = m7 + m6


    n5 = TotalRoomCost.objects.values_list('cabaccrmtotal', flat=True).get(bid_idA=bid_idA)
    n6 = TotalRoomCost.objects.values_list('cabacccustom', flat=True).get(bid_idA=bid_idA)
    n7 = n5 + n6
    TotalRoomCost.objects.filter(bid_idA=instance2).update(cabinet=l4, cabtotalprice=m4, custcabcost=t1,
                                                           custcabtotal=t2, cabsidecost=p5t, cabsidetotal=k5,
                                                           custsidetotal=l5, drawercost=m6b, drawertotal=m7,
                                                           cabacctotal=n7)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute13_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/totalrmcost2.html', context)


def totalrmcost3(request, id=None):
    instance = BidTbl.objects.get(id=id)
    instance2 = BidTbl.objects.values_list('bid_idA', flat=True).get(id=id)
    instance3 = BidTbl.objects.values_list('id', flat=True).get(id=id)
    instance4 = TotalRoomCost.objects.values_list('bid_idA', flat=True).get(bid_idA=instance2)
    form = TotalRmCost(request.POST or None, instance=instance)
    AccOptionTotal.objects.filter(bid_idA=instance2).delete()
    CompOptionTotal.objects.filter(bid_idA=instance2).delete()
    Labor.objects.filter(bid_idA=instance2).delete()
    Cabinet.objects.filter(bid_idA=instance2).delete()
    a = BidTbl.objects.all()
    b = BidTbl2.objects.all()
    aa = Pricing.objects.all()
    cc = Comp.objects.all()
    dd = CabAcc.objects.all()
    ee = CustomerInfo.objects.all()
    ff = TotalRoomCost.objects.values_list('custid', flat=True).get(bid_idA=instance4)
    ffaa = TotalRoomCost.objects.values_list('conid', flat=True).get(bid_idA=instance4)
    ffab = TotalRoomCost.objects.values_list('room_id', flat=True).get(bid_idA=instance4)
    gg = ee.values_list('prodqueue_id', flat=True).get(custid=ff) or 0
    hh = TotalRoomCost.objects.values_list('totalperc', flat=True).get(bid_idA=instance4) or 0
    c = a.filter(bid_idA=instance4).aggregate(Sum('cab1_id')).get('cab1_id__sum') or 0
    d = a.filter(bid_idA=instance4).aggregate(Sum('cab2_id')).get('cab2_id__sum') or 0
    e = a.filter(bid_idA=instance4).aggregate(Sum('cab3_id')).get('cab3_id__sum') or 0
    f = b.filter(bid_idA=instance4).aggregate(Sum('cab4_id')).get('cab4_id__sum') or 0
    g = b.filter(bid_idA=instance4).aggregate(Sum('cab5_id')).get('cab5_id__sum') or 0
    h = b.filter(bid_idA=instance4).aggregate(Sum('cab6_id')).get('cab6_id__sum') or 0
    ii = c + d + e + f + g + h  ## 2
    j4 = aa.values_list('cabinet', flat=True).last()  ## 200
    j4a = aa.values_list('cab_labor', flat=True).last()  ## 300
    k4 = j4 * gg  ### Cabinet Price * Prodqueue = Prod. Increase
    l4 = j4 + k4  ### Cabinet Price + Prodqueue
    m4 = l4 * ii  ### Cabinet Price Total
    n4 = j4 * ii  ### Total Numbers of Cabinets * Cabinet Price ###  400
    Cabinet.objects.create(bid_idA=instance4, custid=ff, conid=ffaa, cabqty=ii, cablabor=j4a)
    c1 = a.filter(bid_idA=instance4).aggregate(Sum('cab1sides_id')).get('cab1sides_id__sum') or 0
    d1 = a.filter(bid_idA=instance4).aggregate(Sum('cab2sides_id')).get('cab2sides_id__sum') or 0
    e1 = a.filter(bid_idA=instance4).aggregate(Sum('cab3sides_id')).get('cab3sides_id__sum') or 0
    f1 = b.filter(bid_idA=instance4).aggregate(Sum('cab4sides_id')).get('cab4sides_id__sum') or 0
    g1 = b.filter(bid_idA=instance4).aggregate(Sum('cab5sides_id')).get('cab5sides_id__sum') or 0
    h1 = b.filter(bid_idA=instance4).aggregate(Sum('cab6sides_id')).get('cab6sides_id__sum') or 0
    i1 = c1 + d1 + e1 + f1 + g1 + h1
    j1 = aa.values_list('sides', flat=True).last()
    o5 = j1 * gg
    p5t = j1 + o5
    k5 = i1 * p5t
    l5 = i1 * j1
    c2 = a.filter(bid_idA=instance4).aggregate(Sum('drwer1_id')).get('drwer1_id__sum') or 0
    d2 = a.filter(bid_idA=instance4).aggregate(Sum('drwer2_id')).get('drwer2_id__sum') or 0
    e2 = a.filter(bid_idA=instance4).aggregate(Sum('drwer3_id')).get('drwer3_id__sum') or 0
    f2 = b.filter(bid_idA=instance4).aggregate(Sum('drwer4_id')).get('drwer4_id__sum') or 0
    g2 = b.filter(bid_idA=instance4).aggregate(Sum('drwer5_id')).get('drwer5_id__sum') or 0
    h2 = b.filter(bid_idA=instance4).aggregate(Sum('drwer6_id')).get('drwer6_id__sum') or 0
    i2 = c2 + d2 + e2 + f2 + g2 + h2
    j2 = aa.values_list('drawer', flat=True).last()
    o6 = j2 * gg
    p6t = j2 + o6
    k6 = i2 * p6t
    data = CompOption.objects.filter(bid_idA=instance4).values('comp', 'bid_idA', 'custid', 'conid', 'roomid', 'compname',
                                                             'labor') \
        .order_by('comp').annotate(compqty=Sum('compqty'), totalprice=Sum('totalprice'), totallabor=Sum('totallabor'))
    w = CompOptionTotal.objects.bulk_create([CompOptionTotal(**q) for q in data])
    x = CompOptionTotal.objects.filter(bid_idA=instance4).aggregate(Sum('totalprice')).get('totalprice__sum') or 0
    Totals.objects.filter(bid_idA=instance2).update(cabaccrmtotal=x)
    p4 = Totals.objects.values_list('cabaccrmtotal', flat=True).get(bid_idA=instance2)
    p5 = p4 * gg
    Totals.objects.filter(bid_idA=instance2).update(cabaccrmtotalincrease=p5)
    p6 = p4 + p5
    Totals.objects.filter(bid_idA=instance2).update(cabaccrmtotaltotal=p6)
    y = CompOptionTotal.objects.filter(bid_idA=instance4).aggregate(Sum('totallabor')).get('totallabor__sum') or 0

    a1 = AccOption.objects.values_list('bid_idA', flat=True).filter(bid_idA=instance4).first()
    data1 = AccOption.objects.filter(bid_idA=a1).values('acc', 'bid_idA', 'custid', 'conid') \
        .order_by('acc').annotate(total_qty=Sum('accqty'), totalprice=Sum('totalprice'))
    ww = AccOptionTotal.objects.bulk_create([AccOptionTotal(**q) for q in data1])
    yy = AccOptionTotal.objects.filter(bid_idA=instance4).aggregate(Sum('totalprice')).get('totalprice__sum') or 0
    Totals.objects.filter(bid_idA=instance2).update(optionnum=yy)
    p1 = Totals.objects.values_list('optionnum', flat=True).get(bid_idA=instance4)
    p2 = p1 * gg
    Totals.objects.filter(bid_idA=instance4).update(optionnumincrease=p2)
    p3 = p1 + p2
    Totals.objects.filter(bid_idA=instance4).update(optionnumtotal=p3)
    objs = BidTbl.objects.filter(bid_idA=instance4)
    objs.update(price=0)
    objs2 = BidTbl2.objects.filter(bid_idA=instance4)
    objs2.update(price=0)
    p = TotalRoomCost.objects.values_list('custcabtotal', flat=True).get(bid_idA=instance4) or 0
    q = TotalRoomCost.objects.values_list('custsidetotal', flat=True).get(bid_idA=instance4) or 0
    r = TotalRoomCost.objects.values_list('drawertotal', flat=True).get(bid_idA=instance4) or 0
    s = TotalRoomCost.objects.values_list('optionnum', flat=True).get(bid_idA=instance4) or 0
    t = TotalRoomCost.objects.values_list('cabacctotal', flat=True).get(bid_idA=instance4) or 0
    t9 = TotalRoomCost.objects.values_list('room_id', flat=True).get(bid_idA=instance4) or 2
    t10 = RoomType.objects.values_list('room_type', flat=True).get(id=t9)
    www = TotalRoomCost.objects.values_list('woodspecies_id', flat=True).get(
        bid_idA=instance4) or WoodSpecies.objects.values_list('id', flat=True).first()
    t2 = WoodSpecies.objects.values_list('woodspecies', flat=True).get(id=www)
    xxx = TotalRoomCost.objects.values_list('doorstyle_id', flat=True).get(
        bid_idA=instance4) or DoorStyle.objects.values_list('id', flat=True).first()
    t4 = DoorStyle.objects.values_list('doorstyle', flat=True).get(id=xxx)
    yyy = TotalRoomCost.objects.values_list('finishcolor_id', flat=True).get(
        bid_idA=instance4) or FinishColor.objects.values_list('id', flat=True).first()
    t6 = FinishColor.objects.values_list('finishcolor', flat=True).get(id=yyy)
    zzz = TotalRoomCost.objects.values_list('finishoption1_id', flat=True).get(
        bid_idA=instance4) or FinishOption.objects.values_list('id', flat=True).first()
    t8 = FinishOption.objects.values_list('finishoption', flat=True).get(id=zzz)
    zzz1 = TotalRoomCost.objects.values_list('finishoption2_id', flat=True).get(
        bid_idA=instance4) or FinishOption.objects.values_list('id', flat=True).first()
    t81 = FinishOption.objects.values_list('finishoption', flat=True).get(id=zzz1)
    totals = p + q + r + s + t
    b30 = CustomerInfo.objects.values_list('prodqueue_id', flat=True).get(id=ff)
    b33 = int(totals)
    b31 = b33 * b30
    b32 = b33 + b31
    CurrentRm.objects.filter(bid_idA=instance4).update(rmcost=b32)

    TotalRoomCost.objects.filter(bid_idA=instance4).update(cabnumtotal=ii, cabinet=l4, cabtotalprice=m4, cabsidenum=i1,
                                                           cabsidecost=p5t, cabsidetotal=k5, drawernum=i2,
                                                           drawercost=p6t, drawertotal=k6, cabaccrmtotal=p6, optionnum=p3,
                                                           woodspecies_id=www, doorstyle_id=xxx,
                                                           finishcolor_id=yyy, finishoption1_id=zzz,
                                                           finishoption2_id=zzz1,
                                                           totalrmcost=b32, prodqueuetotal=b31,
                                                           totallabor=y, rmactive=1, wood=t2, door=t4, fncolor=t6,
                                                           fnoption=t8, fnoption2=t81, rmname=t10)
    z3 = TotalRoomCost.objects.values_list('room_id', flat=True).get(bid_idA=instance4)
    z1a = Cabinet.objects.values_list('cabqty', flat=True).get(bid_idA=instance4) or 0
    z1b = Cabinet.objects.values_list('cablabor', flat=True).get(bid_idA=instance4) or 0

    z1c = z1a * z1b
    Cabinet.objects.filter(bid_idA=instance4).update(totalcablabor=z1c, roomid=ffab)
    Labor.objects.create(custid=ff, conid=ffaa, bid_idA=instance2, room=z3, labor=y, rmactive=1)
    z1 = Pricing.objects.values_list('cab_labor', flat=True).last()
    z2 = ii * z1
    Labor.objects.create(custid=ff, conid=ffaa, bid_idA=instance2, room=z3, labor=z2, rmactive=1)

    cabtotal = TotalRoomCost.objects.values('cabnumtotal').get(bid_idA=instance4)
    cabinet = TotalRoomCost.objects.values('cabinet').get(bid_idA=instance4)
    cabtotalprice = TotalRoomCost.objects.values('cabtotalprice').get(bid_idA=instance4)
    b = TotalRoomCost.objects.values_list('cabtotalprice', flat=True).get(bid_idA=instance4)
    c = TotalRoomCost.objects.values_list('totalperc', flat=True).get(bid_idA=instance4)
    d = b * c
    e = str(d)
    f = float(e)
    g = TotalRoomCost.objects.filter(bid_idA=instance4).update(custcabcost=f)
    h = TotalRoomCost.objects.values_list('custcabcost', flat=True).get(bid_idA=instance4)
    i = TotalRoomCost.objects.values_list('cabtotalprice', flat=True).get(bid_idA=instance4)
    j = h + i
    k = TotalRoomCost.objects.filter(bid_idA=instance4).update(custcabtotal=j)
    custcabcost = TotalRoomCost.objects.values('custcabcost').get(bid_idA=instance4)
    custcabtotal = TotalRoomCost.objects.values('custcabtotal').get(bid_idA=instance4)
    ### Sides ###
    cabsidenum = TotalRoomCost.objects.values('cabsidenum').get(bid_idA=instance4)
    cabsidecost = TotalRoomCost.objects.values('cabsidecost').get(bid_idA=instance4)
    cabsidetotal = TotalRoomCost.objects.values('cabsidetotal').get(bid_idA=instance4)
    bb = TotalRoomCost.objects.values_list('cabsidetotal', flat=True).get(bid_idA=instance4)
    cc = TotalRoomCost.objects.values_list('totalperc', flat=True).get(bid_idA=instance4)
    dd = bb * cc
    ee = str(dd)
    ff = float(ee)
    gg = TotalRoomCost.objects.filter(bid_idA=instance4).update(custsidecost=ff)
    hh = TotalRoomCost.objects.values_list('custsidecost', flat=True).get(bid_idA=instance4)
    ii = TotalRoomCost.objects.values_list('cabsidetotal', flat=True).get(bid_idA=instance4)
    jj = hh + ii
    kk = TotalRoomCost.objects.filter(bid_idA=instance4).update(custsidetotal=jj)
    custcabsidecost = TotalRoomCost.objects.values('custsidecost').get(bid_idA=instance4)
    custcabsidetotal = TotalRoomCost.objects.values('custsidetotal').get(bid_idA=instance4)
    ### Drawers ###
    drawernum = TotalRoomCost.objects.values('drawernum').get(bid_idA=instance4)
    drawercost = TotalRoomCost.objects.values('drawercost').get(bid_idA=instance4)
    drawertotal = TotalRoomCost.objects.values('drawertotal').get(bid_idA=instance4)
    ### Cabinet Accessories ###
    cabaccrmtotal = TotalRoomCost.objects.values('cabaccrmtotal').get(bid_idA=instance4) or 0
    bbb = TotalRoomCost.objects.values_list('cabaccrmtotal', flat=True).get(bid_idA=instance4) or 0
    ccc = TotalRoomCost.objects.values_list('totalperc', flat=True).get(bid_idA=instance4) or 0
    ddd = bbb * ccc
    eee = str(ddd)
    fff = float(eee)
    ggg = TotalRoomCost.objects.filter(bid_idA=instance4).update(cabacccustom=fff)
    hhh = TotalRoomCost.objects.values_list('cabaccrmtotal', flat=True).get(bid_idA=instance4) or 0
    iii = TotalRoomCost.objects.values_list('cabacccustom', flat=True).get(bid_idA=instance4) or 0
    jjj = hhh + iii
    kkk = TotalRoomCost.objects.filter(bid_idA=instance4).update(cabacctotal=jjj)
    t2 = TotalRoomCost.objects.values_list('drawertotal', flat=True).get(bid_idA=instance4) or 0
    t3 = TotalRoomCost.objects.values_list('optionnum', flat=True).get(bid_idA=instance4) or 0
    t4 = TotalRoomCost.objects.values_list('cabacctotal', flat=True).get(bid_idA=instance4) or 0
    t1 = j + jj + t2 + t3 + t4
    TotalRoomCost.objects.filter(bid_idA=instance4).update(rmgrandtotal=t1)

    Totals.objects.filter(bid_idA=instance4).update(baseprice=t1, totalrmcost=t1, rmcost=t1)
    cabacccustom = TotalRoomCost.objects.values('cabacccustom').get(bid_idA=instance4) or 0
    cabacctotal = TotalRoomCost.objects.values('cabacctotal').get(bid_idA=instance4) or 0
    optionnum = TotalRoomCost.objects.values('optionnum').get(bid_idA=instance4) or 0
    totalrmcost1 = TotalRoomCost.objects.values('totalrmcost').get(bid_idA=instance4) or 0
    totalrmcost2 = TotalRoomCost.objects.values('prodqueuetotal').get(bid_idA=instance4) or 0
    totalrmcost3 = TotalRoomCost.objects.values('rmgrandtotal').get(bid_idA=instance4) or 0
    b10 = TotalRoomCost.objects.values_list('rmgrandtotal', flat=True).get(bid_idA=instance4)
    CurrentRm.objects.filter(bid_idA=instance4).update(rmcost=b10)


    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance3.get_absolute11_url())
    context = {
        "instance": instance,
        "form": form,
        "cc": cc,
        "dd": dd,
        "w": w,
        "ww": ww,

        "cabtotal": cabtotal,
        "cabinet": cabinet,
        "cabtotalprice": cabtotalprice,
        "g": g,
        "k": k,
        "custcabtotal": custcabtotal,
        "custcabcost": custcabcost,
        "cabsidenum": cabsidenum,
        "cabsidecost": cabsidecost,
        "cabsidetotal": cabsidetotal,
        "gg": gg,
        "kk": kk,
        "custcabsidecost": custcabsidecost,
        "custcabsidetotal": custcabsidetotal,
        "drawernum": drawernum,
        "drawercost": drawercost,
        "drawertotal": drawertotal,
        "cabaccrmtotal": cabaccrmtotal,
        "cabacccustom": cabacccustom,
        "cabacctotal": cabacctotal,
        "ggg": ggg,
        "kkk": kkk,
        "totalrmcost1": totalrmcost1,
        "totalrmcost2": totalrmcost2,
        "totalrmcost3": totalrmcost3,
        "optionnum": optionnum,
        "t1": t1,

    }

    return redirect(instance.get_absolute11_url(), context)


def woodspecies(request, bid_idA=None):
    instance = get_object_or_404(TotalRoomCost, bid_idA=bid_idA)
    form = TotalRmCost(request.POST or None, instance=instance)
    a = request.POST['id_woodspecies']
    b = WoodSpecies.objects.all()
    c = b.values_list('increase', flat=True).get(id=a)
    t1 = b.values_list('woodspecies', flat=True).get(id=a)
    d = TotalRoomCost.objects.filter(bid_idA=bid_idA).update(woodspecies_id=a, woodspeciesperc=c, wood=t1)
    context = {
        "instance": instance,
        "form": form,
        "d": d,
        "woodspeciesprec": c,
    }
    return render(request, 'wsc/totalrmcost.html', context)


def load_woodspecies(request, bid_idA=None):
    a = TotalRoomCost.objects.all()
    instance = get_object_or_404(TotalRoomCost, bid_idA=bid_idA)
    form = TotalRmCost(request.POST or None, instance=instance)
    c = a.values('woodspecies_id').get(bid_idA=bid_idA)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute13_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
        "woodspecies": woodspecies,

    }
    return render(request, 'wsc/wood_species.html', context)


def load_woodspeciesperc(request, bid_idA=None):
    a = TotalRoomCost.objects.all()
    instance = get_object_or_404(TotalRoomCost, bid_idA=bid_idA)
    form = TotalRmCost(request.POST or None, instance=instance)
    woodperc = a.values('woodspeciesperc').get(bid_idA=bid_idA)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute13_url())
    context = {
        "instance": instance,
        "woodperc": woodperc,
        "form": form,
    }
    return render(request, 'wsc/woodspecies_perc.html', context)


def doorstyle(request, bid_idA=None):
    instance = get_object_or_404(TotalRoomCost, bid_idA=bid_idA)
    form = TotalRmCost(request.POST or None, instance=instance)
    a = request.POST['id_doorstyle']
    b = DoorStyle.objects.all()
    c = b.values_list('increase', flat=True).get(id=a)
    t1 = b.values_list('doorstyle', flat=True).get(id=a)
    d = TotalRoomCost.objects.filter(bid_idA=bid_idA).update(doorstyle_id=a, doorstyleperc=c, door=t1)
    context = {
        "instance": instance,
        "form": form,
        "d": d,
        "doorstyleprec": c,
    }
    return render(request, 'wsc/totalrmcost.html', context)


def load_doorstyle(request, bid_idA=None):
    a = TotalRoomCost.objects.all()
    instance = get_object_or_404(TotalRoomCost, bid_idA=bid_idA)
    form = TotalRmCost(request.POST or None, instance=instance)
    c = a.values('doorstyle_id').get(bid_idA=bid_idA)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute13_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/door_style.html', context)


def load_doorstyleperc(request, bid_idA=None):
    a = TotalRoomCost.objects.all()
    instance = get_object_or_404(TotalRoomCost, bid_idA=bid_idA)
    form = TotalRmCost(request.POST or None, instance=instance)
    styleperc = a.values('doorstyleperc').get(bid_idA=bid_idA)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute13_url())
    context = {
        "instance": instance,
        "styleperc": styleperc,
        "form": form,
    }
    return render(request, 'wsc/doorstyle_perc.html', context)


def finishcolor(request, bid_idA=None):
    instance = get_object_or_404(TotalRoomCost, bid_idA=bid_idA)
    form = TotalRmCost(request.POST or None, instance=instance)
    a = request.POST['id_finishcolor']
    b = FinishColor.objects.all()
    c = b.values_list('increase', flat=True).get(id=a)
    t1 = b.values_list('finishcolor', flat=True).get(id=a)
    d = TotalRoomCost.objects.filter(bid_idA=bid_idA).update(finishcolor_id=a, finishcolorperc=c, fncolor=t1)
    context = {
        "instance": instance,
        "form": form,
        "d": d,
        "finishcolorprec": c,
    }
    return render(request, 'wsc/totalrmcost.html', context)


def load_finishcolor(request, bid_idA=None):
    a = TotalRoomCost.objects.all()
    instance = get_object_or_404(TotalRoomCost, bid_idA=bid_idA)
    form = TotalRmCost(request.POST or None, instance=instance)
    c = a.values('finishcolor_id').get(bid_idA=bid_idA)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute13_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/finish_color.html', context)


def load_finishcolorperc(request, bid_idA=None):
    a = TotalRoomCost.objects.all()
    instance = get_object_or_404(TotalRoomCost, bid_idA=bid_idA)
    form = TotalRmCost(request.POST or None, instance=instance)
    colorperc = a.values('finishcolorperc').get(bid_idA=bid_idA)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute13_url())
    context = {
        "instance": instance,
        "colorperc": colorperc,
        "form": form,
    }
    return render(request, 'wsc/finishcolor_perc.html', context)


def finishoption(request, bid_idA=None):
    instance = get_object_or_404(TotalRoomCost, bid_idA=bid_idA)
    form = TotalRmCost(request.POST or None, instance=instance)
    a = request.POST['id_finishoption1']
    b = FinishOption.objects.all()
    c = b.values_list('increase', flat=True).get(id=a)
    t1 = b.values_list('finishoption', flat=True).get(id=a)
    d = TotalRoomCost.objects.filter(bid_idA=bid_idA).update(finishoption1_id=a, finishoption1perc=c, fnoption=t1)
    context = {
        "instance": instance,
        "form": form,
        "d": d,
        "finishoptionprec": c,
    }
    return render(request, 'wsc/totalrmcost.html', context)


def load_finishoption(request, bid_idA=None):
    a = TotalRoomCost.objects.all()
    instance = get_object_or_404(TotalRoomCost, bid_idA=bid_idA)
    form = TotalRmCost(request.POST or None, instance=instance)
    c = a.values('finishoption1_id').get(bid_idA=bid_idA)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute13_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/finish_option.html', context)

def load_finishoptionperc(request, bid_idA=None):
    a = TotalRoomCost.objects.all()
    instance = get_object_or_404(TotalRoomCost, bid_idA=bid_idA)
    form = TotalRmCost(request.POST or None, instance=instance)
    optionperc = a.values('finishoption1perc').get(bid_idA=bid_idA)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute13_url())
    context = {
        "instance": instance,
        "optionperc": optionperc,
        "form": form,
    }
    return render(request, 'wsc/finishoption_perc.html', context)


def finishoption2(request, bid_idA=None):
    instance = get_object_or_404(TotalRoomCost, bid_idA=bid_idA)
    form = TotalRmCost(request.POST or None, instance=instance)
    a = request.POST['id_finishoption2']
    b = FinishOption.objects.all()
    c = b.values_list('increase', flat=True).get(id=a)
    t1 = b.values_list('finishoption', flat=True).get(id=a)
    d = TotalRoomCost.objects.filter(bid_idA=bid_idA).update(finishoption2_id=a, finishoption2perc=c, fnoption2=t1)
    context = {
        "instance": instance,
        "form": form,
        "d": d,
        "finishoptionprec": c,
    }
    return render(request, 'wsc/totalrmcost.html', context)


def load_finishoption2(request, bid_idA=None):
    a = TotalRoomCost.objects.all()
    instance = get_object_or_404(TotalRoomCost, bid_idA=bid_idA)
    form = TotalRmCost(request.POST or None, instance=instance)
    c = a.values('finishoption2_id').get(bid_idA=bid_idA)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute13_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/finish_option2.html', context)

def load_finishoptionperc2(request, bid_idA=None):
    a = TotalRoomCost.objects.all()
    instance = get_object_or_404(TotalRoomCost, bid_idA=bid_idA)
    form = TotalRmCost(request.POST or None, instance=instance)
    optionperc = a.values('finishoption2perc').get(bid_idA=bid_idA)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute13_url())
    context = {
        "instance": instance,
        "optionperc": optionperc,
        "form": form,
    }
    return render(request, 'wsc/finishoption2_perc.html', context)


def load_totalperc(request, bid_idA=None):
    instance = get_object_or_404(TotalRoomCost, bid_idA=bid_idA)
    form = TotalRmCost(request.POST or None, instance=instance)
    a = TotalRoomCost.objects.all()
    b1 = a.values_list('woodspeciesperc', flat=True).get(bid_idA=bid_idA)
    c1 = a.values_list('doorstyleperc', flat=True).get(bid_idA=bid_idA)
    d1 = a.values_list('finishcolorperc', flat=True).get(bid_idA=bid_idA)
    e1 = a.values_list('finishoption1perc', flat=True).get(bid_idA=bid_idA)
    t1 = a.values_list('finishoption2perc', flat=True).get(bid_idA=bid_idA)
    f = b1 + c1 + d1 + e1 + t1
    g = str(f)
    h = float(g)
    d = TotalRoomCost.objects.filter(bid_idA=bid_idA).update(totalperc=h)
    totalperc = a.values('totalperc').get(bid_idA=bid_idA)
    context = {
        "instance": instance,
        "form": form,
        "d": d,
        "totalperc": totalperc,
    }
    return render(request, 'wsc/total_perc.html', context)


def load_cabinet(request, bid_idA=None):
    instance = get_object_or_404(TotalRoomCost, bid_idA=bid_idA)
    form = TotalRmCost(request.POST or None, instance=instance)
    a = TotalRoomCost.objects.all()
            ### Cabinets ###
    cabtotal = a.values('cabnumtotal').get(bid_idA=bid_idA)
    cabinet = a.values('cabinet').get(bid_idA=bid_idA)
    cabtotalprice = a.values('cabtotalprice').get(bid_idA=bid_idA)
    b = a.values_list('cabtotalprice', flat=True).get(bid_idA=bid_idA)
    c = a.values_list('totalperc', flat=True).get(bid_idA=bid_idA)
    d = b * c
    e = str(d)
    f = float(e)
    g = TotalRoomCost.objects.filter(bid_idA=bid_idA).update(custcabcost=f)
    h = a.values_list('custcabcost', flat=True).get(bid_idA=bid_idA)
    i = a.values_list('cabtotalprice', flat=True).get(bid_idA=bid_idA)
    j = h + i
    k = TotalRoomCost.objects.filter(bid_idA=bid_idA).update(custcabtotal=j)
    custcabcost = a.values('custcabcost').get(bid_idA=bid_idA)
    custcabtotal = a.values('custcabtotal').get(bid_idA=bid_idA)
            ### Sides ###
    cabsidenum = a.values('cabsidenum').get(bid_idA=bid_idA)
    cabsidecost = a.values('cabsidecost').get(bid_idA=bid_idA)
    cabsidetotal = a.values('cabsidetotal').get(bid_idA=bid_idA)
    bb = a.values_list('cabsidetotal', flat=True).get(bid_idA=bid_idA)
    cc = a.values_list('totalperc', flat=True).get(bid_idA=bid_idA)
    dd = bb * cc
    ee = str(dd)
    ff = float(ee)
    gg = TotalRoomCost.objects.filter(bid_idA=bid_idA).update(custsidecost=ff)
    hh = a.values_list('custsidecost', flat=True).get(bid_idA=bid_idA)
    ii = a.values_list('cabsidetotal', flat=True).get(bid_idA=bid_idA)
    jj = hh + ii
    kk = TotalRoomCost.objects.filter(bid_idA=bid_idA).update(custsidetotal=jj)
    custcabsidecost = a.values('custsidecost').get(bid_idA=bid_idA)
    custcabsidetotal = a.values('custsidetotal').get(bid_idA=bid_idA)
            ### Drawers ###
    drawernum = a.values('drawernum').get(bid_idA=bid_idA)
    drawercost = a.values('drawercost').get(bid_idA=bid_idA)
    drawertotal = a.values('drawertotal').get(bid_idA=bid_idA)
            ### Cabinet Accessories ###
    cabaccrmtotal = a.values('cabaccrmtotal').get(bid_idA=bid_idA) or 0
    bbb = a.values_list('cabaccrmtotal', flat=True).get(bid_idA=bid_idA) or 0
    ccc = a.values_list('totalperc', flat=True).get(bid_idA=bid_idA) or 0
    ddd = bbb * ccc
    eee = str(ddd)
    fff = float(eee)
    ggg = TotalRoomCost.objects.filter(bid_idA=bid_idA).update(cabacccustom=fff)
    hhh = a.values_list('cabaccrmtotal', flat=True).get(bid_idA=bid_idA) or 0
    iii = a.values_list('cabacccustom', flat=True).get(bid_idA=bid_idA) or 0
    jjj = hhh + iii
    kkk = TotalRoomCost.objects.filter(bid_idA=bid_idA).update(cabacctotal=jjj)
    t2 = TotalRoomCost.objects.values_list('drawertotal', flat=True).get(bid_idA=bid_idA) or 0
    t3 = TotalRoomCost.objects.values_list('optionnum', flat=True).get(bid_idA=bid_idA) or 0
    t4 = TotalRoomCost.objects.values_list('cabacctotal', flat=True).get(bid_idA=bid_idA) or 0
    t1 = j + jj + t2 + t3 + t4
    TotalRoomCost.objects.filter(bid_idA=bid_idA).update(rmgrandtotal=t1)

    Totals.objects.filter(bid_idA=bid_idA).update(baseprice=t1, totalrmcost=t1, rmcost=t1)
    cabacccustom = a.values('cabacccustom').get(bid_idA=bid_idA) or 0
    cabacctotal = a.values('cabacctotal').get(bid_idA=bid_idA) or 0
    optionnum = a.values('optionnum').get(bid_idA=bid_idA) or 0
    totalrmcost1 = a.values('totalrmcost').get(bid_idA=bid_idA) or 0
    totalrmcost2 = a.values('prodqueuetotal').get(bid_idA=bid_idA) or 0
    totalrmcost3 = a.values('rmgrandtotal').get(bid_idA=bid_idA) or 0
    b10 = a.values_list('rmgrandtotal', flat=True).get(bid_idA=bid_idA)
    CurrentRm.objects.filter(bid_idA=bid_idA).update(rmcost=b10)

    context = {
        "instance": instance,
        "form": form,
        "cabtotal": cabtotal,
        "cabinet": cabinet,
        "cabtotalprice": cabtotalprice,
        "g": g,
        "k": k,
        "custcabtotal": custcabtotal,
        "custcabcost": custcabcost,
        "cabsidenum": cabsidenum,
        "cabsidecost": cabsidecost,
        "cabsidetotal": cabsidetotal,
        "gg": gg,
        "kk": kk,
        "custcabsidecost": custcabsidecost,
        "custcabsidetotal": custcabsidetotal,
        "drawernum": drawernum,
        "drawercost": drawercost,
        "drawertotal": drawertotal,
        "cabaccrmtotal": cabaccrmtotal,
        "cabacccustom": cabacccustom,
        "cabacctotal": cabacctotal,
        "ggg": ggg,
        "kkk": kkk,
        "totalrmcost1": totalrmcost1,
        "totalrmcost2": totalrmcost2,
        "totalrmcost3": totalrmcost3,
        "optionnum": optionnum,
        "t1": t1,

    }
    return render(request, 'wsc/cab_cost.html', context)



def load_cabinet2(request, bid_idA=None):
    instance = get_object_or_404(TotalRoomCost, bid_idA=bid_idA)
    form = TotalRmCost(request.POST or None, instance=instance)
    a = TotalRoomCost.objects.all()
            ### Cabinets ###
    cabtotal = a.values('cabnumtotal').get(bid_idA=bid_idA)
    cabinet = a.values('cabinet').get(bid_idA=bid_idA)
    cabtotalprice = a.values('cabtotalprice').get(bid_idA=bid_idA)
    b = a.values_list('cabtotalprice', flat=True).get(bid_idA=bid_idA)
    c = a.values_list('totalperc', flat=True).get(bid_idA=bid_idA)
    d = b * c
    e = str(d)
    f = float(e)
    g = TotalRoomCost.objects.filter(bid_idA=bid_idA).update(custcabcost=f)
    h = a.values_list('custcabcost', flat=True).get(bid_idA=bid_idA)
    i = a.values_list('cabtotalprice', flat=True).get(bid_idA=bid_idA)
    j = h + i
    k = TotalRoomCost.objects.filter(bid_idA=bid_idA).update(custcabtotal=j)
    custcabcost = a.values('custcabcost').get(bid_idA=bid_idA)
    custcabtotal = a.values('custcabtotal').get(bid_idA=bid_idA)
            ### Sides ###
    cabsidenum = a.values('cabsidenum').get(bid_idA=bid_idA)
    cabsidecost = a.values('cabsidecost').get(bid_idA=bid_idA)
    cabsidetotal = a.values('cabsidetotal').get(bid_idA=bid_idA)
    bb = a.values_list('cabsidetotal', flat=True).get(bid_idA=bid_idA)
    cc = a.values_list('totalperc', flat=True).get(bid_idA=bid_idA)
    dd = bb * cc
    ee = str(dd)
    ff = float(ee)
    gg = TotalRoomCost.objects.filter(bid_idA=bid_idA).update(custsidecost=ff)
    hh = a.values_list('custsidecost', flat=True).get(bid_idA=bid_idA)
    ii = a.values_list('cabsidetotal', flat=True).get(bid_idA=bid_idA)
    jj = hh + ii
    kk = TotalRoomCost.objects.filter(bid_idA=bid_idA).update(custsidetotal=jj)
    custcabsidecost = a.values('custsidecost').get(bid_idA=bid_idA)
    custcabsidetotal = a.values('custsidetotal').get(bid_idA=bid_idA)
            ### Drawers ###
    drawernum = a.values('drawernum').get(bid_idA=bid_idA)
    drawercost = a.values('drawercost').get(bid_idA=bid_idA)
    drawertotal = a.values('drawertotal').get(bid_idA=bid_idA)
            ### Cabinet Accessories ###
    cabaccrmtotal = a.values('cabaccrmtotal').get(bid_idA=bid_idA) or 0
    bbb = a.values_list('cabaccrmtotal', flat=True).get(bid_idA=bid_idA) or 0
    ccc = a.values_list('totalperc', flat=True).get(bid_idA=bid_idA) or 0
    ddd = bbb * ccc
    eee = str(ddd)
    fff = float(eee)
    ggg = TotalRoomCost.objects.filter(bid_idA=bid_idA).update(cabacccustom=fff)
    hhh = a.values_list('cabaccrmtotal', flat=True).get(bid_idA=bid_idA) or 0
    iii = a.values_list('cabacccustom', flat=True).get(bid_idA=bid_idA) or 0
    jjj = hhh + iii
    kkk = TotalRoomCost.objects.filter(bid_idA=bid_idA).update(cabacctotal=jjj)
    t2 = TotalRoomCost.objects.values_list('drawertotal', flat=True).get(bid_idA=bid_idA) or 0
    t3 = TotalRoomCost.objects.values_list('optionnum', flat=True).get(bid_idA=bid_idA) or 0
    t4 = TotalRoomCost.objects.values_list('cabacctotal', flat=True).get(bid_idA=bid_idA) or 0
    t1 = j + jj + t2 + t3 + t4
    TotalRoomCost.objects.filter(bid_idA=bid_idA).update(rmgrandtotal=t1)

    t5 = TotalRoomCost.objects.values_list('cabnumtotal', flat=True).get(bid_idA=bid_idA)
    t6 = Pricing.objects.values_list('cabinet', flat=True).last()
    t7 = t5 * t6
    t8 = TotalRoomCost.objects.values_list('cabsidenum', flat=True).get(bid_idA=bid_idA)
    t9 = Pricing.objects.values_list('sides', flat=True).last()
    t10 = t8 * t9
    t11 = Totals.objects.values_list('cabaccrmtotal', flat=True).get(bid_idA=bid_idA)
    t13 = t7 + t10 + t11
    t14 = TotalRoomCost.objects.values_list('totalperc', flat=True).get(bid_idA=bid_idA)
    t15 = t13 * t14
    t16 = t13 + t15
    t17 = TotalRoomCost.objects.values_list('drawernum', flat=True).get(bid_idA=bid_idA)
    t18 = Pricing.objects.values_list('drawer', flat=True).last()
    t19 = t17 * t18
    t20 = Totals.objects.values_list('optionnum', flat=True).get(bid_idA=bid_idA)
    t21 = t16 + t19 + t20
    t22 = Totals.objects.filter(bid_idA=bid_idA).update(baseprice=t21, rmcost=t21)

    Totals.objects.filter(bid_idA=bid_idA).update(totalrmcost=t1)
    cabacccustom = a.values('cabacccustom').get(bid_idA=bid_idA) or 0
    cabacctotal = a.values('cabacctotal').get(bid_idA=bid_idA) or 0
    optionnum = a.values('optionnum').get(bid_idA=bid_idA) or 0
    totalrmcost1 = Totals.objects.values('rmcost').get(bid_idA=bid_idA) or 0
    totalrmcost2 = a.values('prodqueuetotal').get(bid_idA=bid_idA) or 0
    totalrmcost3 = a.values('rmgrandtotal').get(bid_idA=bid_idA) or 0
    b10 = a.values_list('rmgrandtotal', flat=True).get(bid_idA=bid_idA)
    CurrentRm.objects.filter(bid_idA=bid_idA).update(rmcost=b10)

    context = {
        "instance": instance,
        "form": form,
        "cabtotal": cabtotal,
        "cabinet": cabinet,
        "cabtotalprice": cabtotalprice,
        "g": g,
        "k": k,
        "custcabtotal": custcabtotal,
        "custcabcost": custcabcost,
        "cabsidenum": cabsidenum,
        "cabsidecost": cabsidecost,
        "cabsidetotal": cabsidetotal,
        "gg": gg,
        "kk": kk,
        "custcabsidecost": custcabsidecost,
        "custcabsidetotal": custcabsidetotal,
        "drawernum": drawernum,
        "drawercost": drawercost,
        "drawertotal": drawertotal,
        "cabaccrmtotal": cabaccrmtotal,
        "cabacccustom": cabacccustom,
        "cabacctotal": cabacctotal,
        "ggg": ggg,
        "kkk": kkk,
        "totalrmcost1": totalrmcost1,
        "totalrmcost2": totalrmcost2,
        "totalrmcost3": totalrmcost3,
        "optionnum": optionnum,
        "t22": t22,

    }
    return render(request, 'wsc/cab_cost.html', context)



def appendcurrm(request, bid_idA=None):
    instance = get_object_or_404(TotalRoomCost, bid_idA=bid_idA)
    form = TotalRmCost(request.POST or None, instance=instance)
    a = TotalRoomCost.objects.all()
    c = TotalRoomCost.objects.values_list('totalrmcost', flat=True).get(bid_idA=bid_idA) or 0
    instance3 = TotalRoomCost.objects.values_list('custid', flat=True).get(bid_idA=bid_idA) or 0
    d = str(c)
###    CurrentRm.objects.filter(bid_idA=bid_idA).update(rmcost=d)
###    Totals.objects.filter(bid_idA=bid_idA).update(rmcost=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance3.get_absolute21_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "a": a,
    }
    return render(request, 'wsc/custinfo.html', context)


def rmselection(request, bid_idA=None):
    instance = CurrentRm.objects.get(bid_idA=bid_idA)
    form = RmSelection(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute17_url(), context2)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/rmselection.html', context)


def bidpageselection(request, id=None):
    instance = get_object_or_404(BidTbl, id=id)
    form = BidPageSelection(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute17a_url(), context2)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/bidpageselection.html', context)


def addtocontract(request, bid_idA=None):
    instance = CurrentRm.objects.get(bid_idA=bid_idA)
    form = RmSelection(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return render(request, 'wsc/custinfo.html', context2)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/addtocontract.html', context)


def yescontract(request, bid_idA=None):
    instance = CurrentRm.objects.get(bid_idA=bid_idA)
    form = RmSelection(request.POST or None, instance=instance)
    CurrentRm.objects.filter(bid_idA=bid_idA).update(rmactive=1)
    BidTbl.objects.filter(bid_idA=bid_idA).update(rmactive=1)
    TotalRoomCost.objects.filter(bid_idA=bid_idA).update(rmactive=1)
    Labor.objects.filter(bid_idA=bid_idA).update(rmactive=1)
    ContractInclude.objects.filter(bid_idA=bid_idA).update(rmactive=1)
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute24_url(), context)

def nocontract(request, bid_idA=None):
    instance = CurrentRm.objects.get(bid_idA=bid_idA)
    form = RmSelection(request.POST or None, instance=instance)
    CurrentRm.objects.filter(bid_idA=bid_idA).update(rmactive=0)
    BidTbl.objects.filter(bid_idA=bid_idA).update(rmactive=0)
    TotalRoomCost.objects.filter(bid_idA=bid_idA).update(rmactive=0)
    Labor.objects.filter(bid_idA=bid_idA).update(rmactive=0)
    ContractInclude.objects.filter(bid_idA=bid_idA).update(rmactive=0)
    context = {
        "instance": instance,
        "form": form,

    }
    return redirect(instance.get_absolute24_url(), context)


def deleterm(request, bid_idA=None):
    instance = TotalRoomCost.objects.get(bid_idA=bid_idA)
    form = RmSelection(request.POST or None, instance=instance)
    aa = TotalRoomCost.objects.values_list('custid', flat=True).get(bid_idA=bid_idA)
    bb = DeleteRm.objects.create(deleterm=aa)
    instance2 = DeleteRm.objects.order_by('deleterm').last()
    a = CurrentRm.objects.all()
    b = BidTbl.objects.all()
    c = BidTbl2.objects.all()
    d = AccOption.objects.all()
    e = AccOptionTotal.objects.all()
    f = CompOption.objects.all()
    g = CompOptionTotal.objects.all()
    h = TotalRoomCost.objects.all()
    i = Totals.objects.all()
    ii = Labor.objects.all()
    t1 = ContractInclude.objects.all()
    t2 = ContractIncludeTotal.objects.all()
    t3 = Cabinet.objects.all()
    a.filter(bid_idA=bid_idA).delete()
    b.filter(bid_idA=bid_idA).delete()
    c.filter(bid_idA=bid_idA).delete()
    d.filter(bid_idA=bid_idA).delete()
    e.filter(bid_idA=bid_idA).delete()
    f.filter(bid_idA=bid_idA).delete()
    g.filter(bid_idA=bid_idA).delete()
    h.filter(bid_idA=bid_idA).delete()
    i.filter(bid_idA=bid_idA).delete()
    ii.filter(bid_idA=bid_idA).delete()
    t1.filter(bid_idA=bid_idA).delete()
    t2.filter(bid_idA=bid_idA).delete()
    t3.filter(bid_idA=bid_idA).delete()
    context = {
        "instance": instance,
        "form": form,
        "bb": bb,
    }
    return redirect(instance2.get_absolute36_url(), context)


def deleterm1(request, bid_idA=None):
    instance = TotalRoomCost.objects.get(bid_idA=bid_idA)
    form = RmSelection(request.POST or None, instance=instance)
    DeleteRm.objects.all().delete()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute21_url(), context2)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/deleterm1.html', context)

def deleterm2(request, bid_idA=None):
    instance = TotalRoomCost.objects.get(bid_idA=bid_idA)
    form = RmSelection(request.POST or None, instance=instance)
    a = CurrentRm.objects.all()
    b = BidTbl.objects.all()
    c = BidTbl2.objects.all()
    d = AccOption.objects.all()
    e = AccOptionTotal.objects.all()
    f = CompOption.objects.all()
    g = CompOptionTotal.objects.all()
    h = TotalRoomCost.objects.all()
    a.filter(bid_idA=bid_idA).delete()
    b.filter(bid_idA=bid_idA).delete()
    c.filter(bid_idA=bid_idA).delete()
    d.filter(bid_idA=bid_idA).delete()
    e.filter(bid_idA=bid_idA).delete()
    f.filter(bid_idA=bid_idA).delete()
    g.filter(bid_idA=bid_idA).delete()
    h.filter(bid_idA=bid_idA).delete()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return render(request, 'wsc/custinfo.html')
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/custinfo.html', context)


def existingrm(request, bid_idA=None):
    instance = BidTbl.objects.get(bid_idA=bid_idA)
    form = BidPage(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute21_url(), context2)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/existingrm.html', context)


def deletermtable(request):
    DeleteRm.objects.all().delete()

    return render(request, 'wsc/deleterm1.html')


def jobcost(request, id):
    global t13, p, v, t6, t7, t8, t9
    instance = JobCost.objects.get(custid=id)
    form = JobCostForm(request.POST or None, instance=instance)
    a = CurrentRm.objects.all()
    d = JobCost.objects.all()
    d1 = ContractIncludeTotal.objects.filter(custid=id).delete()

    b = a.filter(custid=id, rmactive=1).aggregate(Sum('rmcost')).get('rmcost__sum') or 0
    c = JobCost.objects.filter(custid=id).update(totalrmcost=b)
    totalrmcost = d.values('totalrmcost').get(custid=id)
    custom = d.values('custom').get(custid=id)
    discount = d.values('discount').get(custid=id)
    construction = d.values('construction').get(custid=id)
    opt2 = d.values('opt2').get(custid=id)
    opt3 = d.values('opt3').get(custid=id)
    f = JobCost.objects.values_list('custom', flat=True).get(custid=id)
    g = JobCost.objects.values_list('discount', flat=True).get(custid=id)
    h = f + g + b
    i = JobCost.objects.filter(custid=id).update(subtotalcost=h)
    t4 = Labor.objects.filter(custid=id, rmactive=1).aggregate(Sum('labor')).get('labor__sum')
    t5 = JobCost.objects.values_list('installtext_id', flat=True).get(custid=id)
    if t5 == 0:
        JobCost.objects.filter(custid=id).update(installrate=0, installtext_id=2, install='No')
        k = TaxRate.objects.values_list('tax', flat=True).last()
        l = float(k)
        m = JobCost.objects.values_list('subtotalcost', flat=True).get(custid=id)
        n = int(m)
        o = l * n
        i = JobCost.objects.filter(custid=id).update(subtotalcost=h, tax=o, taxrate=k)
    elif t5 == 1:
        t6 = JobCost.objects.filter(custid=id).update(installrate=t4)
        k = 0
        o = 0
        i = JobCost.objects.filter(custid=id).update(subtotalcost=h, tax=o, taxrate=k)
        t7 = JobCost.objects.values_list('id', flat=True).last()
        t8 = Labor.objects.filter(custid=id, rmactive=1).aggregate(Sum('labor')).get('labor__sum')
        t9 = JobCost.objects.filter(custid=id).update(installrate=t8)
    elif t5 == 2:
        JobCost.objects.filter(custid=id).update(installrate=0)
        k = TaxRate.objects.values_list('tax', flat=True).last()
        l = float(k)
        m = JobCost.objects.values_list('subtotalcost', flat=True).get(custid=id)
        n = int(m)
        o = l * n
        i = JobCost.objects.filter(custid=id).update(subtotalcost=h, tax=o, taxrate=k)
    installrate = JobCost.objects.values('installrate').get(custid=id)
    subtotalcost = d.values('subtotalcost').get(custid=id)
    taxrate = TaxRate.objects.values('taxperc').last()
    tax = d.values('tax').get(custid=id)
    totaljobcost = d.values('totaljobcost').get(custid=id)
    grandtotalcost = JobCost.objects.values('grandtotalcost').get(custid=id)
    data = ContractInclude.objects.filter(custid=id, rmactive=1).values('custid', 'conid', 'name', 'rmactive').order_by(
        'name').annotate(qty=Sum('qty'), includeid=Sum('includeid'))
    w = ContractIncludeTotal.objects.bulk_create([ContractIncludeTotal(**q) for q in data])

    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "i": i,
        "totalrmcost": totalrmcost,
        "custom": custom,
        "discount": discount,
        "construction": construction,
        "opt2": opt2,
        "opt3": opt3,
        "subtotalcost": subtotalcost,
        "taxrate": taxrate,
        "totaljobcost": totaljobcost,
        "tax": tax,
        "grandtotalcost": grandtotalcost,
        "w": w,
        "d1": d1,
        "installrate": installrate,

    }
    return render(request, 'wsc/jobcost.html', context)


def load_subtotalcost(request, custid=None):
    a = JobCost.objects.all()
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    subtotalcost = a.values('subtotalcost').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "subtotalcost": subtotalcost,
        "instance": instance,
        "form": form,

    }
    return render(request, 'wsc/sub_total.html', context)


def tax(request, custid=None):
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    a = TaxRate.objects.values_list('tax', flat=True).last()
    b = float(a)
    c = JobCost.objects.values_list('subtotalcost', flat=True).get(custid=custid)
    d = int(c)
    e = b * d
    f = JobCost.objects.filter(custid=custid).update(tax=e)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "e": e,

    }
    return render(request, 'wsc/jobcost.html', context)



def load_tax(request, custid=None):
    a = JobCost.objects.all()
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    tax = a.values('tax').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "tax": tax,
        "instance": instance,
        "form": form,

    }
    return render(request, 'wsc/tax.html', context)


def load_totaljobcost(request, custid=None):
    a = JobCost.objects.all()
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    totaljobcost = a.values('totaljobcost').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "totaljobcost": totaljobcost,
        "instance": instance,
        "form": form,

    }
    return render(request, 'wsc/total_jobcost.html', context)


def load_grandtotalcost(request, custid=None):
    a = JobCost.objects.all()
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    grandtotalcost = a.values('grandtotalcost').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "grandtotalcost": grandtotalcost,
        "instance": instance,
        "form": form,

    }
    return render(request, 'wsc/grand_totalcost.html', context)


def customtext(request, custid=None):
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    a = request.POST['id_customtext']
    d = JobCost.objects.filter(custid=custid).update(customtext=a)
    context = {
        "instance": instance,
        "form": form,
        "d": d,
    }
    return render(request, 'wsc/jobcost.html', context)


def load_customtext(request, custid=None):
    a = JobCost.objects.all()
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    customtext = a.values('customtext').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "customtext": customtext,
        "instance": instance,
        "form": form,

    }
    return render(request, 'wsc/custom_text.html', context)


def custom(request, custid=None):
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    a = request.POST['id_customamount']
    b = JobCost.objects.filter(custid=custid).update(custom=a)
    c = JobCost.objects.values_list('totalrmcost', flat=True).get(custid=custid)
    d = JobCost.objects.values_list('custom', flat=True).get(custid=custid)
    e = JobCost.objects.values_list('discount', flat=True).get(custid=custid)
    f = c + d + e
    g = JobCost.objects.filter(custid=custid).update(subtotalcost=f)
    h = JobCost.objects.values_list('taxrate', flat=True).get(custid=custid)
    i = h * f
    j = f + i
    k = JobCost.objects.filter(custid=custid).update(tax=i, totaljobcost=j)
    l = JobCost.objects.values_list('construction', flat=True).get(custid=custid)
    m = JobCost.objects.values_list('opt2', flat=True).get(custid=custid)
    n = JobCost.objects.values_list('opt3', flat=True).get(custid=custid)
    o = JobCost.objects.values_list('installrate', flat=True).get(custid=custid)
    p = l + m + n + o
    q = j + p
    r = JobCost.objects.filter(custid=custid).update(grandtotalcost=q)

    context = {
        "instance": instance,
        "form": form,
        "g": g,
        "b": b,
        "k": k,
        "r": r,
    }
    return render(request, 'wsc/jobcost.html', context)


def custom1(request, custid=None):
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    c = JobCost.objects.values_list('totalrmcost', flat=True).get(custid=custid)
    d = JobCost.objects.values_list('custom', flat=True).get(custid=custid)
    e = JobCost.objects.values_list('discount', flat=True).get(custid=custid)
    f = c + d + e
    g = JobCost.objects.filter(custid=custid).update(subtotalcost=f)
    h = JobCost.objects.values_list('taxrate', flat=True).get(custid=custid)
    i = h * f
    j = f + i
    k = JobCost.objects.filter(custid=custid).update(tax=i, totaljobcost=j)
    l = JobCost.objects.values_list('construction', flat=True).get(custid=custid)
    m = JobCost.objects.values_list('opt2', flat=True).get(custid=custid)
    n = JobCost.objects.values_list('opt3', flat=True).get(custid=custid)
    o = JobCost.objects.values_list('installrate', flat=True).get(custid=custid)
    p = l + m + n + o
    q = j + p
    r = JobCost.objects.filter(custid=custid).update(grandtotalcost=q)

    context = {
        "instance": instance,
        "form": form,
        "g": g,
        "k": k,
        "r": r,
    }
    return render(request, 'wsc/jobcost.html', context)


def load_custom(request, custid=None):
    a = JobCost.objects.all()
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    customa = a.values('custom').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "customa": customa,
        "instance": instance,
        "form": form,

    }
    return render(request, 'wsc/custom_amount.html', context)


def discounttext(request, custid=None):
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    a = request.POST['id_discounttext']
    d = JobCost.objects.filter(custid=custid).update(discounttext_id=a)
    context = {
        "instance": instance,
        "form": form,
        "d": d,
    }
    return render(request, 'wsc/jobcost.html', context)


def load_discounttext(request, custid=None):
    a = JobCost.objects.all()
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    discounttext = a.values('discounttext').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "discounttext": discounttext,
        "instance": instance,
        "form": form,

    }
    return render(request, 'wsc/discount_text.html', context)


def discount(request, custid=None):
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    a = request.POST['id_discountamount']
    b = JobCost.objects.filter(custid=custid).update(discount=a)
    c = JobCost.objects.values_list('totalrmcost', flat=True).get(custid=custid)
    d = JobCost.objects.values_list('custom', flat=True).get(custid=custid)
    e = JobCost.objects.values_list('discount', flat=True).get(custid=custid)
    f = c + d + e
    g = JobCost.objects.filter(custid=custid).update(subtotalcost=f)
    h = JobCost.objects.values_list('taxrate', flat=True).get(custid=custid)
    i = h * f
    j = f + i
    k = JobCost.objects.filter(custid=custid).update(tax=i, totaljobcost=j)
    l = JobCost.objects.values_list('construction', flat=True).get(custid=custid)
    m = JobCost.objects.values_list('opt2', flat=True).get(custid=custid)
    n = JobCost.objects.values_list('opt3', flat=True).get(custid=custid)
    o = JobCost.objects.values_list('installrate', flat=True).get(custid=custid)
    p = l + m + n + o
    q = j + p
    r = JobCost.objects.filter(custid=custid).update(grandtotalcost=q)

    context = {
        "instance": instance,
        "form": form,
        "g": g,
        "b": b,
        "k": k,
        "r": r,
    }
    return render(request, 'wsc/jobcost.html', context)


def load_discount(request, custid=None):
    a = JobCost.objects.all()
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    discounta = a.values('discount').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "discounta": discounta,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/discount_amount.html', context)


def constructiontext(request, custid=None):
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    a = request.POST['id_constructiontext']
    d = JobCost.objects.filter(custid=custid).update(constructiontext_id=a)
    context = {
        "instance": instance,
        "form": form,
        "d": d,
    }
    return render(request, 'wsc/jobcost.html', context)


def load_constructiontext(request, custid=None):
    a = JobCost.objects.all()
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    constructiontext = a.values('constructiontext_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "constructiontext": constructiontext,
        "instance": instance,
        "form": form,

    }
    return render(request, 'wsc/construction_text.html', context)


def construction(request, custid=None):
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    a = request.POST['id_constructionamount']
    b = JobCost.objects.filter(custid=custid).update(construction=a)
    c = JobCost.objects.values_list('totaljobcost', flat=True).get(custid=custid)
    d = JobCost.objects.values_list('construction', flat=True).get(custid=custid)
    e = JobCost.objects.values_list('opt2', flat=True).get(custid=custid)
    f = JobCost.objects.values_list('opt3', flat=True).get(custid=custid)
    g = JobCost.objects.values_list('installrate', flat=True).get(custid=custid)
    h = c + d + e + f + g
    i = JobCost.objects.filter(custid=custid).update(grandtotalcost=h)
    context = {
        "instance": instance,
        "form": form,
        "g": g,
        "b": b,
        "i": i,
    }
    return render(request, 'wsc/jobcost.html', context)


def load_construction(request, custid=None):
    a = JobCost.objects.all()
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    constructiona = a.values('construction').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "constructiona": constructiona,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/construction_amount.html', context)


def opt2text(request, custid=None):
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    a = request.POST['id_opt2text']
    d = JobCost.objects.filter(custid=custid).update(opt2text_id=a)
    context = {
        "instance": instance,
        "form": form,
        "d": d,
    }
    return render(request, 'wsc/jobcost.html', context)




def load_opt2text(request, custid=None):
    a = JobCost.objects.all()
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    opt2text = a.values('opt2text_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "opt2text": opt2text,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/opt2_text.html', context)


def opt2(request, custid=None):
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    a = request.POST['id_opt2amount']
    b = JobCost.objects.filter(custid=custid).update(opt2=a)
    c = JobCost.objects.values_list('totaljobcost', flat=True).get(custid=custid)
    d = JobCost.objects.values_list('construction', flat=True).get(custid=custid)
    e = JobCost.objects.values_list('opt2', flat=True).get(custid=custid)
    f = JobCost.objects.values_list('opt3', flat=True).get(custid=custid)
    g = JobCost.objects.values_list('installrate', flat=True).get(custid=custid)
    h = c + d + e + f + g
    i = JobCost.objects.filter(custid=custid).update(grandtotalcost=h)
    context = {
        "instance": instance,
        "form": form,
        "g": g,
        "b": b,
        "i": i,
    }
    return render(request, 'wsc/jobcost.html', context)


def load_opt2(request, custid=None):
    a = JobCost.objects.all()
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    opt2a = a.values('opt2').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "opt2a": opt2a,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/opt2_amount.html', context)


def opt3text(request, custid=None):
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    a = request.POST['id_opt3text']
    b = JobCost.objects.filter(custid=custid).update(opt3text_id=a)
    c = JobCost.objects.values_list('totaljobcost', flat=True).get(custid=custid)
    d = JobCost.objects.values_list('construction', flat=True).get(custid=custid)
    e = JobCost.objects.values_list('opt2', flat=True).get(custid=custid)
    f = JobCost.objects.values_list('opt3', flat=True).get(custid=custid)
    g = JobCost.objects.values_list('installrate', flat=True).get(custid=custid)
    h = c + d + e + f + g
    i = JobCost.objects.filter(custid=custid).update(grandtotalcost=h)
    context = {
        "instance": instance,
        "form": form,
        "g": g,
        "b": b,
        "i": i,
    }
    return render(request, 'wsc/jobcost.html', context)




def load_opt3text(request, custid=None):
    a = JobCost.objects.all()
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    opt3text = a.values('opt3text_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "opt3text": opt3text,
        "instance": instance,
        "form": form,

    }
    return render(request, 'wsc/opt3_text.html', context)


def opt3(request, custid=None):
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    a = request.POST['id_opt3amount']
    b = JobCost.objects.filter(custid=custid).update(opt3=a)
    c = JobCost.objects.values_list('totaljobcost', flat=True).get(custid=custid)
    d = JobCost.objects.values_list('construction', flat=True).get(custid=custid)
    e = JobCost.objects.values_list('opt2', flat=True).get(custid=custid)
    f = JobCost.objects.values_list('opt3', flat=True).get(custid=custid)
    g = JobCost.objects.values_list('installrate', flat=True).get(custid=custid)
    h = c + d + e + f + g
    i = JobCost.objects.filter(custid=custid).update(grandtotalcost=h)
    context = {
        "instance": instance,
        "form": form,
        "g": g,
        "b": b,
        "i": i,
    }
    return render(request, 'wsc/jobcost.html', context)


def load_opt3(request, custid=None):
    a = JobCost.objects.all()
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    opt3a = a.values('opt3').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "opt3a": opt3a,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/opt3_amount.html', context)


def load_install(request, custid=None):
    a = JobCost.objects.all()
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    install = a.values('install').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "opt3text": opt3text,
        "instance": instance,
        "form": form,
        "install": install,

    }
    return render(request, 'wsc/install_text.html', context)


def installtext(request, custid=None):
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    a = request.POST['id_installtext']
    d = JobCost.objects.filter(custid=custid).update(install_id=a)
    context = {
        "instance": instance,
        "form": form,
        "d": d,
    }
    return render(request, 'wsc/jobcost.html', context)




def load_installtext(request, custid=None):
    a = JobCost.objects.all()
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    installtexta = a.values('installtext').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "installtexta": installtexta,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/install_text.html', context)


def installyes(request, custid=None):
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    a = 0
    b = TaxRate.objects.values_list('tax', flat=True).last()
    c = JobCost.objects.filter(custid=custid).update(tax=a, taxrate=b)
    d = JobCost.objects.values_list('subtotalcost', flat=True).get(custid=custid)
    e = Labor.objects.filter(custid=custid, rmactive=1).aggregate(Sum('labor')).get('labor__sum')
    f = JobCost.objects.filter(custid=custid).update(totaljobcost=d)
    g = JobCost.objects.values_list('construction', flat=True).get(custid=custid)
    h = JobCost.objects.values_list('opt2', flat=True).get(custid=custid)
    i = JobCost.objects.values_list('opt3', flat=True).get(custid=custid)
    j = d + e + g + h + i
    k = JobCost.objects.filter(custid=custid).update(grandtotalcost=j, installrate=e, installtext_id=1, install='Yes')
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "f": f,
        "k": k,
    }
    return render(request, 'wsc/install_rate.html', context)


def installno(request, custid=None):
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    a = 0
    b = TaxRate.objects.values_list('tax', flat=True).last()
    c = float(b)
    d = JobCost.objects.values_list('subtotalcost', flat=True).get(custid=custid)
    e = int(d)
    f = c * e
    g = JobCost.objects.filter(custid=custid).update(tax=f, taxrate=b)

    h = JobCost.objects.values_list('subtotalcost', flat=True).get(custid=custid)
    i = JobCost.objects.values_list('taxrate', flat=True).get(custid=custid)
    j = h * i
    k = h + j
    l = JobCost.objects.filter(custid=custid).update(totaljobcost=k)
    m = JobCost.objects.values_list('construction', flat=True).get(custid=custid)
    n = JobCost.objects.values_list('opt2', flat=True).get(custid=custid)
    o = JobCost.objects.values_list('opt3', flat=True).get(custid=custid)
    p = m + n + o
    q = k + p
    r = JobCost.objects.filter(custid=custid).update(grandtotalcost=q, installrate=a, installtext_id=2, install='No')
    context = {
        "instance": instance,
        "form": form,
        "r": r,
        "d": d,
        "g": g,
        "l": l,
    }
    return render(request, 'wsc/install_rate.html', context)


def load_installrate(request, custid=None):
    a = JobCost.objects.all()
    instance = get_object_or_404(JobCost, custid=custid)
    form = JobCostForm(request.POST or None, instance=instance)
    installratea = a.values('installrate').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "installratea": installratea,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/install_rate.html', context)


def laborbd(request, custid=None):
    global cabtotal
    a = Cabinet.objects.all()
    b = RoomType.objects.all()
    c = CompOptionTotal.objects.all()
    d = Comp.objects.all()
    d1 = BidTbl.objects.all()
    instance = BidTbl.objects.filter(custid=custid).first()
    form = CompLabor(request.POST or None, instance=instance)
    conid = c.values('conid').filter(custid=custid).distinct()
    e = d1.values_list('room_id', flat=True).filter(custid=custid).distinct()
    u = BidTbl.objects.filter(custid=custid).annotate(bid=F('bid_idA'))
    g = list(u.values_list('bid_idA', flat=True))
    f1 = int(e[0])
    roomid1 = RoomType.objects.values_list('room_type', flat=True).get(idA=f1)
    bid_idA1 = g[0]
    cab1qty = Cabinet.objects.values_list('cabqty', flat=True).get(bid_idA=g[0])
    cab1labor = Cabinet.objects.values_list('cablabor', flat=True).get(bid_idA=g[0])
    cab1total = Cabinet.objects.values_list('totalcablabor', flat=True).get(bid_idA=g[0])
    cot = CompOptionTotal.objects.filter(bid_idA=g[0]).aggregate(Sum('totallabor')).get('totallabor__sum') or 0
    trl1 = cab1total + cot
    comp1 = CompOptionTotal.objects.filter(bid_idA=g[0])
    try:
        f2 = int(e[1])
        roomid2 = b.values_list('room_type', flat=True).get(idA=f2)
        bid_idA2 = g[1]
        cab2qty = Cabinet.objects.values_list('cabqty', flat=True).get(bid_idA=g[1])
        cab2labor = Cabinet.objects.values_list('cablabor', flat=True).get(bid_idA=g[1])
        cab2total = Cabinet.objects.values_list('totalcablabor', flat=True).get(bid_idA=g[1])
        cot2 = CompOptionTotal.objects.filter(bid_idA=g[1]).aggregate(Sum('totallabor')).get('totallabor__sum') or 0
        trl2 = cab2total + cot2
        comp2 = CompOptionTotal.objects.filter(bid_idA=g[1])
    except Exception:
        f2 = 0
        roomid2 = '------------'
        bid_idA2 = '---'
        cab2qty = 0
        cab2labor = 0
        cab2total = 0
        comp2 = CompOptionTotal.objects.filter(bid_idA=0)
        trl2 = '------------'
    try:
        f3 = int(e[2])
        roomid3 = b.values_list('room_type', flat=True).get(idA=f3)
        bid_idA3 = g[2]
        cab3qty = Cabinet.objects.values_list('cabqty', flat=True).get(bid_idA=g[2])
        cab3labor = Cabinet.objects.values_list('cablabor', flat=True).get(bid_idA=g[2])
        cab3total = Cabinet.objects.values_list('totalcablabor', flat=True).get(bid_idA=g[2])
        cot3 = CompOptionTotal.objects.filter(bid_idA=g[2]).aggregate(Sum('totallabor')).get('totallabor__sum') or 0
        trl3 = cab3total + cot3
        comp3 = CompOptionTotal.objects.filter(bid_idA=g[2])
    except Exception:
        f3 = 0
        roomid3 = '------------'
        bid_idA3 = '---'
        cab3qty = 0
        cab3labor = 0
        cab3total = 0
        comp3 = CompOptionTotal.objects.filter(bid_idA=0)
        trl3 = '------------'
    try:
        f4 = int(e[3])
        roomid4 = b.values_list('room_type', flat=True).get(idA=f4)
        bid_idA4 = g[3]
        cab4qty = Cabinet.objects.values_list('cabqty', flat=True).get(bid_idA=g[3])
        cab4labor = Cabinet.objects.values_list('cablabor', flat=True).get(bid_idA=g[3])
        cab4total = Cabinet.objects.values_list('totalcablabor', flat=True).get(bid_idA=g[3])
        cot4 = CompOptionTotal.objects.filter(bid_idA=g[3]).aggregate(Sum('totallabor')).get('totallabor__sum') or 0
        trl4 = cab4total + cot4
        comp4 = CompOptionTotal.objects.filter(bid_idA=g[3])
    except Exception:
        f4 = 0
        roomid4 = '------------'
        bid_idA4 = '---'
        cab4qty = 0
        cab4labor = 0
        cab4total = 0
        comp4 = CompOptionTotal.objects.filter(bid_idA=0)
        trl4 = '------------'
    try:
        f5 = int(e[4])
        roomid5 = b.values_list('room_type', flat=True).get(idA=f5)
        bid_idA5 = g[4]
        cab5qty = Cabinet.objects.values_list('cabqty', flat=True).get(bid_idA=g[4])
        cab5labor = Cabinet.objects.values_list('cablabor', flat=True).get(bid_idA=g[4])
        cab5total = Cabinet.objects.values_list('totalcablabor', flat=True).get(bid_idA=g[4])
        cot5 = CompOptionTotal.objects.filter(bid_idA=g[4]).aggregate(Sum('totallabor')).get('totallabor__sum') or 0
        trl5 = cab5total + cot5
        comp5 = CompOptionTotal.objects.filter(bid_idA=g[4])
    except Exception:
        f5 = 0
        roomid5 = '------------'
        bid_idA5 = '---'
        cab5qty = 0
        cab5labor = 0
        cab5total = 0
        comp5 = CompOptionTotal.objects.filter(bid_idA=0)
        trl5 = '------------'
    try:
        f6 = int(e[5])
        roomid6 = b.values_list('room_type', flat=True).get(idA=f6)
        bid_idA6 = g[5]
        cab6qty = Cabinet.objects.values_list('cabqty', flat=True).get(bid_idA=g[5])
        cab6labor = Cabinet.objects.values_list('cablabor', flat=True).get(bid_idA=g[5])
        cab6total = Cabinet.objects.values_list('totalcablabor', flat=True).get(bid_idA=g[5])
        cot6 = CompOptionTotal.objects.filter(bid_idA=g[5]).aggregate(Sum('totallabor')).get('totallabor__sum') or 0
        trl6 = cab6total + cot6
        comp6 = CompOptionTotal.objects.filter(bid_idA=g[5])
    except Exception:
        f6 = 0
        roomid6 = '------------'
        bid_idA6 = '---'
        cab6qty = 0
        cab6labor = 0
        cab6total = 0
        comp6 = CompOptionTotal.objects.filter(bid_idA=0)
        trl6 = '------------'
    context = {
        "a": a,
        "d": d,
        "d1": d1,
        "instance": instance,
        "form": form,
        "conid": conid,
        "f1": f1,
        "roomid1": roomid1,
        "bid_idA1": bid_idA1,
        "cab1qty": cab1qty,
        "cab1labor": cab1labor,
        "cab1total": cab1total,
        "trl1": trl1,
        "comp1": comp1,
        "f2": f2,
        "roomid2": roomid2,
        "bid_idA2": bid_idA2,
        "cab2qty": cab2qty,
        "cab2labor": cab2labor,
        "cab2total": cab2total,
        "trl2": trl2,
        "comp2": comp2,
        "f3": f3,
        "roomid3": roomid3,
        "bid_idA3": bid_idA3,
        "cab3qty": cab3qty,
        "cab3labor": cab3labor,
        "cab3total": cab3total,
        "trl3": trl3,
        "comp3": comp3,
        "f4": f4,
        "roomid4": roomid4,
        "bid_idA4": bid_idA4,
        "cab4qty": cab4qty,
        "cab4labor": cab4labor,
        "cab4total": cab4total,
        "trl4": trl4,
        "comp4": comp4,
        "f5": f5,
        "roomid5": roomid5,
        "bid_idA5": bid_idA5,
        "cab5qty": cab5qty,
        "cab5labor": cab5labor,
        "cab5total": cab5total,
        "trl5": trl5,
        "comp5": comp5,
        "f6": f6,
        "roomid6": roomid6,
        "bid_idA6": bid_idA6,
        "cab6qty": cab6qty,
        "cab6labor": cab6labor,
        "cab6total": cab6total,
        "trl6": trl6,
        "comp6": comp6,
    }
    return render(request, 'wsc/laborbd.html', context)


def laborbd2(request, custid=None):
    global cabtotal
    a = Cabinet.objects.all()
    b = RoomType.objects.all()
    c = CompOptionTotal.objects.all()
    d = Comp.objects.all()
    d1 = BidTbl.objects.all()
    instance = BidTbl.objects.filter(custid=custid).first()
    form = CompLabor(request.POST or None, instance=instance)
    conid = c.values('conid').filter(custid=custid).distinct()
    e = d1.values_list('room_id', flat=True).filter(custid=custid).distinct()
    u = BidTbl.objects.filter(custid=custid).annotate(bid=F('bid_idA'))
    g = list(u.values_list('bid_idA', flat=True))
    try:
        f1 = int(e[6])
        roomid1 = RoomType.objects.values_list('room_type', flat=True).get(idA=f1)
        bid_idA1 = g[6]
        cab1qty = Cabinet.objects.values_list('cabqty', flat=True).get(bid_idA=g[6])
        cab1labor = Cabinet.objects.values_list('cablabor', flat=True).get(bid_idA=g[6])
        cab1total = Cabinet.objects.values_list('totalcablabor', flat=True).get(bid_idA=g[6])
        cot = CompOptionTotal.objects.filter(bid_idA=g[6]).aggregate(Sum('totallabor')).get('totallabor__sum') or 0
        trl1 = cab1total + cot
        comp1 = CompOptionTotal.objects.filter(bid_idA=g[6])
    except Exception:
        f1 = 0
        roomid1 = '------------'
        bid_idA1 = '---'
        cab1qty = 0
        cab1labor = 0
        cab1total = 0
        comp1 = CompOptionTotal.objects.filter(bid_idA=0)
        trl1 = '------------'

    try:
        f2 = int(e[7])
        roomid2 = b.values_list('room_type', flat=True).get(idA=f2)
        bid_idA2 = g[7]
        cab2qty = Cabinet.objects.values_list('cabqty', flat=True).get(bid_idA=g[7])
        cab2labor = Cabinet.objects.values_list('cablabor', flat=True).get(bid_idA=g[7])
        cab2total = Cabinet.objects.values_list('totalcablabor', flat=True).get(bid_idA=g[7])
        cot2 = CompOptionTotal.objects.filter(bid_idA=g[7]).aggregate(Sum('totallabor')).get('totallabor__sum') or 0
        trl2 = cab2total + cot2
        comp2 = CompOptionTotal.objects.filter(bid_idA=g[7])
    except Exception:
        f2 = 0
        roomid2 = '------------'
        bid_idA2 = '---'
        cab2qty = 0
        cab2labor = 0
        cab2total = 0
        comp2 = CompOptionTotal.objects.filter(bid_idA=0)
        trl2 = '------------'
    try:
        f3 = int(e[8])
        roomid3 = b.values_list('room_type', flat=True).get(idA=f3)
        bid_idA3 = g[8]
        cab3qty = Cabinet.objects.values_list('cabqty', flat=True).get(bid_idA=g[8])
        cab3labor = Cabinet.objects.values_list('cablabor', flat=True).get(bid_idA=g[8])
        cab3total = Cabinet.objects.values_list('totalcablabor', flat=True).get(bid_idA=g[8])
        cot3 = CompOptionTotal.objects.filter(bid_idA=g[8]).aggregate(Sum('totallabor')).get('totallabor__sum') or 0
        trl3 = cab3total + cot3
        comp3 = CompOptionTotal.objects.filter(bid_idA=g[8])
    except Exception:
        f3 = 0
        roomid3 = '------------'
        bid_idA3 = '---'
        cab3qty = 0
        cab3labor = 0
        cab3total = 0
        comp3 = CompOptionTotal.objects.filter(bid_idA=0)
        trl3 = '------------'
    try:
        f4 = int(e[9])
        roomid4 = b.values_list('room_type', flat=True).get(idA=f4)
        bid_idA4 = g[9]
        cab4qty = Cabinet.objects.values_list('cabqty', flat=True).get(bid_idA=g[9])
        cab4labor = Cabinet.objects.values_list('cablabor', flat=True).get(bid_idA=g[9])
        cab4total = Cabinet.objects.values_list('totalcablabor', flat=True).get(bid_idA=g[9])
        cot4 = CompOptionTotal.objects.filter(bid_idA=g[9]).aggregate(Sum('totallabor')).get('totallabor__sum') or 0
        trl4 = cab4total + cot4
        comp4 = CompOptionTotal.objects.filter(bid_idA=g[9])
    except Exception:
        f4 = 0
        roomid4 = '------------'
        bid_idA4 = '---'
        cab4qty = 0
        cab4labor = 0
        cab4total = 0
        comp4 = CompOptionTotal.objects.filter(bid_idA=0)
        trl4 = '------------'
    try:
        f5 = int(e[10])
        roomid5 = b.values_list('room_type', flat=True).get(idA=f5)
        bid_idA5 = g[10]
        cab5qty = Cabinet.objects.values_list('cabqty', flat=True).get(bid_idA=g[10])
        cab5labor = Cabinet.objects.values_list('cablabor', flat=True).get(bid_idA=g[10])
        cab5total = Cabinet.objects.values_list('totalcablabor', flat=True).get(bid_idA=g[10])
        cot5 = CompOptionTotal.objects.filter(bid_idA=g[10]).aggregate(Sum('totallabor')).get('totallabor__sum') or 0
        trl5 = cab5total + cot5
        comp5 = CompOptionTotal.objects.filter(bid_idA=g[10])
    except Exception:
        f5 = 0
        roomid5 = '------------'
        bid_idA5 = '---'
        cab5qty = 0
        cab5labor = 0
        cab5total = 0
        comp5 = CompOptionTotal.objects.filter(bid_idA=0)
        trl5 = '------------'
    try:
        f6 = int(e[11])
        roomid6 = b.values_list('room_type', flat=True).get(idA=f6)
        bid_idA6 = g[11]
        cab6qty = Cabinet.objects.values_list('cabqty', flat=True).get(bid_idA=g[11])
        cab6labor = Cabinet.objects.values_list('cablabor', flat=True).get(bid_idA=g[11])
        cab6total = Cabinet.objects.values_list('totalcablabor', flat=True).get(bid_idA=g[11])
        cot6 = CompOptionTotal.objects.filter(bid_idA=g[11]).aggregate(Sum('totallabor')).get('totallabor__sum') or 0
        trl6 = cab6total + cot6
        comp6 = CompOptionTotal.objects.filter(bid_idA=g[11])
    except Exception:
        f6 = 0
        roomid6 = '------------'
        bid_idA6 = '---'
        cab6qty = 0
        cab6labor = 0
        cab6total = 0
        comp6 = CompOptionTotal.objects.filter(bid_idA=0)
        trl6 = '------------'
    context = {
        "a": a,
        "d": d,
        "d1": d1,
        "instance": instance,
        "form": form,
        "conid": conid,
        "f1": f1,
        "roomid1": roomid1,
        "bid_idA1": bid_idA1,
        "cab1qty": cab1qty,
        "cab1labor": cab1labor,
        "cab1total": cab1total,
        "trl1": trl1,
        "comp1": comp1,
        "f2": f2,
        "roomid2": roomid2,
        "bid_idA2": bid_idA2,
        "cab2qty": cab2qty,
        "cab2labor": cab2labor,
        "cab2total": cab2total,
        "trl2": trl2,
        "comp2": comp2,
        "f3": f3,
        "roomid3": roomid3,
        "bid_idA3": bid_idA3,
        "cab3qty": cab3qty,
        "cab3labor": cab3labor,
        "cab3total": cab3total,
        "trl3": trl3,
        "comp3": comp3,
        "f4": f4,
        "roomid4": roomid4,
        "bid_idA4": bid_idA4,
        "cab4qty": cab4qty,
        "cab4labor": cab4labor,
        "cab4total": cab4total,
        "trl4": trl4,
        "comp4": comp4,
        "f5": f5,
        "roomid5": roomid5,
        "bid_idA5": bid_idA5,
        "cab5qty": cab5qty,
        "cab5labor": cab5labor,
        "cab5total": cab5total,
        "trl5": trl5,
        "comp5": comp5,
        "f6": f6,
        "roomid6": roomid6,
        "bid_idA6": bid_idA6,
        "cab6qty": cab6qty,
        "cab6labor": cab6labor,
        "cab6total": cab6total,
        "trl6": trl6,
        "comp6": comp6,
    }
    return render(request, 'wsc/laborbd2.html', context)

def laborbd3(request, custid=None):
    global cabtotal
    a = Cabinet.objects.all()
    b = RoomType.objects.all()
    c = CompOptionTotal.objects.all()
    d = Comp.objects.all()
    d1 = BidTbl.objects.all()
    instance = BidTbl.objects.filter(custid=custid).first()
    form = CompLabor(request.POST or None, instance=instance)
    conid = c.values('conid').filter(custid=custid).distinct()
    e = d1.values_list('room_id', flat=True).filter(custid=custid).distinct()
    u = BidTbl.objects.filter(custid=custid).annotate(bid=F('bid_idA'))
    g = list(u.values_list('bid_idA', flat=True))
    f1 = int(e[0])
    roomid1 = RoomType.objects.values_list('room_type', flat=True).get(idA=f1)
    bid_idA1 = g[0]
    cab1qty = Cabinet.objects.values_list('cabqty', flat=True).get(bid_idA=g[0])
    cab1labor = Cabinet.objects.values_list('cablabor', flat=True).get(bid_idA=g[0])
    cab1total = Cabinet.objects.values_list('totalcablabor', flat=True).get(bid_idA=g[0])
    cot = CompOptionTotal.objects.filter(bid_idA=g[0]).aggregate(Sum('totallabor')).get('totallabor__sum') or 0
    trl1 = cab1total + cot
    comp1 = CompOptionTotal.objects.filter(bid_idA=g[0])
    try:
        f2 = int(e[12])
        roomid2 = b.values_list('room_type', flat=True).get(idA=f2)
        bid_idA2 = g[12]
        cab2qty = Cabinet.objects.values_list('cabqty', flat=True).get(bid_idA=g[12])
        cab2labor = Cabinet.objects.values_list('cablabor', flat=True).get(bid_idA=g[12])
        cab2total = Cabinet.objects.values_list('totalcablabor', flat=True).get(bid_idA=g[12])
        cot2 = CompOptionTotal.objects.filter(bid_idA=g[12]).aggregate(Sum('totallabor')).get('totallabor__sum') or 0
        trl2 = cab2total + cot2
        comp2 = CompOptionTotal.objects.filter(bid_idA=g[12])
    except Exception:
        f2 = 0
        roomid2 = '------------'
        bid_idA2 = '---'
        cab2qty = 0
        cab2labor = 0
        cab2total = 0
        comp2 = CompOptionTotal.objects.filter(bid_idA=0)
        trl2 = '------------'

    context = {
        "a": a,
        "d": d,
        "d1": d1,
        "instance": instance,
        "form": form,
        "conid": conid,
        "f1": f1,
        "roomid1": roomid1,
        "bid_idA1": bid_idA1,
        "cab1qty": cab1qty,
        "cab1labor": cab1labor,
        "cab1total": cab1total,
        "trl1": trl1,
        "comp1": comp1,
        "f2": f2,
        "roomid2": roomid2,
        "bid_idA2": bid_idA2,
        "cab2qty": cab2qty,
        "cab2labor": cab2labor,
        "cab2total": cab2total,
        "trl2": trl2,
        "comp2": comp2,

    }
    return render(request, 'wsc/laborbd3.html', context)


def totallabor(request, custid=None):
    instance = get_object_or_404(JobCost, custid=custid)
    form = CompLabor(request.POST or None, instance=instance)
    cab1qty = Cabinet.objects.filter(custid=custid).aggregate(Sum('cabqty')).get('cabqty__sum')
    cab1labor = Cabinet.objects.values_list('cablabor', flat=True).first()
    cab1total = Cabinet.objects.filter(custid=custid).aggregate(Sum('totalcablabor')).get('totalcablabor__sum')
    totallaborcost = JobCost.objects.values('installrate').get(custid=custid)
    a = CompOptionTotal.objects.filter(custid=custid).annotate(job=F('id'))
    b = list(a.values_list('id', flat=True))
    try:
        comp1 = CompOptionTotal.objects.filter(custid=custid, id=b[0])
    except Exception:
        comp1 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp2 = CompOptionTotal.objects.filter(custid=custid, id=b[1])
    except Exception:
        comp2 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp3 = CompOptionTotal.objects.filter(custid=custid, id=b[2])
    except Exception:
        comp3 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp4 = CompOptionTotal.objects.filter(custid=custid, id=b[3])
    except Exception:
        comp4 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp5 = CompOptionTotal.objects.filter(custid=custid, id=b[4])
    except Exception:
        comp5 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp6 = CompOptionTotal.objects.filter(custid=custid, id=b[5])
    except Exception:
        comp6 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp7 = CompOptionTotal.objects.filter(custid=custid, id=b[6])
    except Exception:
        comp7 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp8 = CompOptionTotal.objects.filter(custid=custid, id=b[7])
    except Exception:
        comp8 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp9 = CompOptionTotal.objects.filter(custid=custid, id=b[8])
    except Exception:
        comp9 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp10 = CompOptionTotal.objects.filter(custid=custid, id=b[9])
    except Exception:
        comp10 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp11 = CompOptionTotal.objects.filter(custid=custid, id=b[10])
    except Exception:
        comp11 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp12 = CompOptionTotal.objects.filter(custid=custid, id=b[11])
    except Exception:
        comp12 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp13 = CompOptionTotal.objects.filter(custid=custid, id=b[12])
    except Exception:
        comp13 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp14 = CompOptionTotal.objects.filter(custid=custid, id=b[13])
    except Exception:
        comp14 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp15 = CompOptionTotal.objects.filter(custid=custid, id=b[14])
    except Exception:
        comp15 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp16 = CompOptionTotal.objects.filter(custid=custid, id=b[15])
    except Exception:
        comp16 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp17 = CompOptionTotal.objects.filter(custid=custid, id=b[16])
    except Exception:
        comp17 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp18 = CompOptionTotal.objects.filter(custid=custid, id=b[17])
    except Exception:
        comp18 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp19 = CompOptionTotal.objects.filter(custid=custid, id=b[18])
    except Exception:
        comp19 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp20 = CompOptionTotal.objects.filter(custid=custid, id=b[19])
    except Exception:
        comp20 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp21 = CompOptionTotal.objects.filter(custid=custid, id=b[20])
    except Exception:
        comp21 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp22 = CompOptionTotal.objects.filter(custid=custid, id=b[21])
    except Exception:
        comp22 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp23 = CompOptionTotal.objects.filter(custid=custid, id=b[22])
    except Exception:
        comp23 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp24 = CompOptionTotal.objects.filter(custid=custid, id=b[23])
    except Exception:
        comp24 = CompOptionTotal.objects.filter(custid=custid, id=0)
    try:
        comp25 = CompOptionTotal.objects.filter(custid=custid, id=b[24])
    except Exception:
        comp25 = CompOptionTotal.objects.filter(custid=custid, id=0)

    context = {
        "instance": instance,
        "form": form,
        "comp1": comp1,
        "comp2": comp2,
        "comp3": comp3,
        "comp4": comp4,
        "comp5": comp5,
        "comp6": comp6,
        "comp7": comp7,
        "comp8": comp8,
        "comp9": comp9,
        "comp10": comp10,
        "comp11": comp11,
        "comp12": comp12,
        "comp13": comp13,
        "comp14": comp14,
        "comp15": comp15,
        "comp16": comp16,
        "comp17": comp17,
        "comp18": comp18,
        "comp19": comp19,
        "comp20": comp20,
        "comp21": comp21,
        "comp22": comp22,
        "comp23": comp23,
        "comp24": comp24,
        "comp25": comp25,
        "cab1qty": cab1qty,
        "cab1total": cab1total,
        "cab1labor": cab1labor,
        "totallaborcost": totallaborcost,

    }
    return render(request, 'wsc/totallabor.html', context)





def contract(request, custid=None):
    instance = CustomerInfo.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    queryset = CustomerInfo.objects.filter(custid=custid)
    queryset16 = Contract.objects.filter(custid=custid)
    a = TotalRoomCost.objects.filter(custid=custid).annotate(bid=F('bid_idA'))
    b = list(a.values_list('bid_idA', flat=True))
    IncludedOption.objects.filter(custid=custid).delete()
    IncludedAcc.objects.filter(custid=custid).delete()
#    conid = Contract.objects.values_list('conid', flat=True).get(custid=custid)
    queryset1 = TotalRoomCost.objects.filter(custid=custid, rmactive=1)
    queryset2 = JobCost.objects.filter(custid=custid)
    try:
        t10 = JobCost.objects.values_list('customtext_id', flat=True).get(custid=custid)
        customtext = ContractOption.objects.values_list('conoption', flat=True).get(id=t10)
    except Exception:
        customtext = '----------------'
    try:
        t11 = JobCost.objects.values_list('discounttext_id', flat=True).get(custid=custid)
        discounttext = ContractOption.objects.values_list('conoption', flat=True).get(id=t11)
    except Exception:
        discounttext = '----------------'
    try:
        t12 = JobCost.objects.values_list('constructiontext_id', flat=True).get(custid=custid)
        constructiontext = ContractOption.objects.values_list('conoption', flat=True).get(id=t12)
    except Exception:
        constructiontext = '----------------'
    try:
        t13 = JobCost.objects.values_list('opt2text_id', flat=True).get(custid=custid)
        opt2text = ContractOption.objects.values_list('conoption', flat=True).get(id=t13)
    except Exception:
        opt2text = '----------------'
    try:
        t14 = JobCost.objects.values_list('opt3text_id', flat=True).get(custid=custid)
        opt3text = ContractOption.objects.values_list('conoption', flat=True).get(id=t14)
    except Exception:
        opt3text = '----------------'
    try:
        t15 = JobCost.objects.values_list('grandtotalcost', flat=True).get(custid=custid)
        grandtotalcost = num2words(t15, to='currency', currency='USD')
    except Exception:
        grandtotalcost = '----------------'

    queryset1o = ContractIncludeTotal.objects.annotate(odd=F('id') % 2).filter(odd=True, custid=custid, rmactive=1)
    queryset1e = ContractIncludeTotal.objects.annotate(odd=F('id') % 2).filter(odd=False, custid=custid, rmactive=1)
    querysetlegally5 = Legally5.objects.all()
    querysetlegally1 = Legally1.objects.all()
    querysetlegally2 = Legally2.objects.all()
    querysetlegally3 = Legally3.objects.all()
    querysetlegally4 = Legally4.objects.all()

    context = {
        "instance": instance,
        "form": form,
        "b ": b,
        "object_list": queryset,
        "object_list1": queryset1,
        "object_list1e": queryset1e,
        "object_list1o": queryset1o,
        "object_list2": queryset2,
        "object_list16": queryset16,
#        "conid": conid,
        "customtext": customtext,
        "discounttext": discounttext,
        "constructiontext": constructiontext,
        "opt2text": opt2text,
        "opt3text": opt3text,
        "object_listlegally1": querysetlegally1,
        "object_listlegally2": querysetlegally2,
        "object_listlegally3": querysetlegally3,
        "object_listlegally4": querysetlegally4,
        "object_listlegally5": querysetlegally5,
        "grandtotalcost": grandtotalcost,

    }
    return render(request, 'wsc/contract.html', context)


def workorderdate(request, custid=None):
    instance = CustomerInfo.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_workorderdate']
    e = Contract.objects.filter(custid=custid).update(workorderdate=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,
    }
    return render(request, 'wsc/contract.html', context)


def load_workorderdate(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('workorderdate').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute13_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/work_order_date.html', context)


def worktype(request, custid=None):
    instance = CustomerInfo.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_worktype']
    e = Contract.objects.filter(custid=custid).update(worktype_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_worktype(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('worktype_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute13_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/work_type.html', context)


def memo1(request, custid=None):
    instance = CustomerInfo.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_memo1']
    e = Contract.objects.filter(custid=custid).update(memo1_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,
    }
    return render(request, 'wsc/contract.html', context)


def load_memo1(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    memo1 = a.values('memo1_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "memo1": memo1,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/memo_1.html', context)


def memo2(request, custid=None):
    instance = CustomerInfo.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_memo2']
    e = Contract.objects.filter(custid=custid).update(memo2_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_memo2(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('memo2_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/memo_2.html', context)


def memo3(request, custid=None):
    instance = CustomerInfo.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_memo3']
    e = Contract.objects.filter(custid=custid).update(memo3_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_memo3(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('memo3_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/memo_3.html', context)


def memo4(request, custid=None):
    instance = CustomerInfo.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_memo4']
    e = Contract.objects.filter(custid=custid).update(memo4_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_memo4(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('memo4_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/memo_4.html', context)


def memo5(request, custid=None):
    instance = CustomerInfo.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_memo5']
    e = Contract.objects.filter(custid=custid).update(memo5_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_memo5(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('memo5_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/memo_5.html', context)


def memo6(request, custid=None):
    instance = CustomerInfo.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_memo6']
    e = Contract.objects.filter(custid=custid).update(memo6_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_memo6(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('memo6_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/memo_6.html', context)


def memo7(request, custid=None):
    instance = CustomerInfo.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_memo7']
    e = Contract.objects.filter(custid=custid).update(memo7_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_memo7(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('memo7_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/memo_7.html', context)


def memo8(request, custid=None):
    instance = CustomerInfo.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_memo8']
    e = Contract.objects.filter(custid=custid).update(memo8_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_memo8(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('memo8_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/memo_8.html', context)


def memo9(request, custid=None):
    instance = CustomerInfo.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_memo9']
    e = Contract.objects.filter(custid=custid).update(memo9_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_memo9(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('memo9_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/memo_9.html', context)


def memo10(request, custid=None):
    instance = CustomerInfo.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_memo10']
    e = Contract.objects.filter(custid=custid).update(memo10_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_memo10(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('memo10_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/memo_10.html', context)


def memo11(request, custid=None):
    instance = CustomerInfo.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_memo11']
    e = Contract.objects.filter(custid=custid).update(memo11_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_memo11(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('memo11_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/memo_11.html', context)


def memo12(request, custid=None):
    instance = CustomerInfo.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_memo12']
    e = Contract.objects.filter(custid=custid).update(memo12_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_memo12(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('memo12_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/memo_12.html', context)


def memo13(request, custid=None):
    instance = CustomerInfo.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_memo13']
    e = Contract.objects.filter(custid=custid).update(memo13_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_memo13(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('memo13_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/memo_13.html', context)


def memo14(request, custid=None):
    instance = CustomerInfo.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_memo14']
    e = Contract.objects.filter(custid=custid).update(memo14_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_memo14(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('memo14_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/memo_14.html', context)


def memo15(request, custid=None):
    instance = CustomerInfo.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_memo15']
    e = Contract.objects.filter(custid=custid).update(memo15_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_memo15(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('memo15_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/memo_15.html', context)


def memo16(request, custid=None):
    instance = CustomerInfo.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_memo16']
    e = Contract.objects.filter(custid=custid).update(memo16_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_memo16(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('memo16_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/memo_16.html', context)


def memo17(request, custid=None):
    instance = CustomerInfo.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_memo17']
    e = Contract.objects.filter(custid=custid).update(memo17_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_memo17(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('memo17_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/memo_17.html', context)


def depositperc(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['depositperc']
    e = Contract.objects.filter(custid=custid).update(depositperc_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_depositperc(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('depositperc_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/deposit_perc.html', context)


def payment2perc(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['payment2perc']
    e = Contract.objects.filter(custid=custid).update(pay2perc_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_payment2perc(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('pay2perc_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/pay2_perc.html', context)


def payment3perc(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['payment3perc']
    e = Contract.objects.filter(custid=custid).update(pay3perc_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_payment3perc(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('pay3perc_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/pay3_perc.html', context)


def payment4perc(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['payment4perc']
    e = Contract.objects.filter(custid=custid).update(pay4perc_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_payment4perc(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('pay4perc_id').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/pay4_perc.html', context)


def depositterms(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['depositterms']
    e = Contract.objects.filter(custid=custid).update(depositterms_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_depositterms(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('depositterms').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/deposit_terms.html', context)


def terms2(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['terms2']
    e = Contract.objects.filter(custid=custid).update(terms2=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_terms2(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('terms2').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/terms_2.html', context)


def terms3(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['terms3']
    e = Contract.objects.filter(custid=custid).update(terms3=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_terms3(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('terms3').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/terms_3.html', context)


def terms4(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['terms4']
    e = Contract.objects.filter(custid=custid).update(terms4=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_terms4(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('terms4').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/terms_4.html', context)


def termsfinal(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['termsfinal']
    e = Contract.objects.filter(custid=custid).update(termsfinal=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'wsc/contract.html', context)


def load_termsfinal(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('termsfinal').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/terms_final.html', context)


def load_depositamount(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    deposita = a.values('deposit').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "deposita": deposita,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/deposit_amount.html', context)


def customdeposit(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_customdeposit']
    f = Contract.objects.filter(custid=custid).update(deposit=d)
    a = JobCost.objects.values_list('grandtotalcost', flat=True).get(custid=custid)
    b = Contract.objects.values_list('deposit', flat=True).get(custid=custid)
    c = a-b
    g = Contract.objects.filter(custid=custid).update(finalpayment=c)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "g": g,

    }
    return render(request, 'wsc/contract.html', context)


def cdp(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_depositperc']
    f = Contract.objects.filter(custid=custid).update(depositperc_id=d)
    g = JobCost.objects.values_list('grandtotalcost', flat=True).get(custid=custid)
    h = Contract.objects.values_list('depositperc_id', flat=True).get(custid=custid)
    i = g * h
    j = Contract.objects.filter(custid=custid).update(deposit=i)
    k = Contract.objects.values_list('deposit', flat=True).get(custid=custid)
    l = g-k
    m = Contract.objects.filter(custid=custid).update(finalpayment=l)
    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "m": m,
        "j": j,
    }
    return render(request, 'wsc/contract.html', context)


def seconddeposit(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_seconddeposit']
    f = Contract.objects.filter(custid=custid).update(payment2=d)
    a = JobCost.objects.values_list('grandtotalcost', flat=True).get(custid=custid)
    b = Contract.objects.values_list('deposit', flat=True).get(custid=custid)
    b2 = Contract.objects.values_list('payment2', flat=True).get(custid=custid)
    c = a-b-b2
    g = Contract.objects.filter(custid=custid).update(finalpayment=c)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "g": g,

    }
    return render(request, 'wsc/contract.html', context)


def load_secondamount(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    payment2a = a.values('payment2').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "payment2a": payment2a,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/second_payment.html', context)


def secdp(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_pay2perc']
    f = Contract.objects.filter(custid=custid).update(pay2perc_id=d)
    g = JobCost.objects.values_list('grandtotalcost', flat=True).get(custid=custid)
    h = Contract.objects.values_list('pay2perc_id', flat=True).get(custid=custid)
    i = g * h
    j = Contract.objects.filter(custid=custid).update(payment2=i)
    k = Contract.objects.values_list('deposit', flat=True).get(custid=custid)
    k2 = Contract.objects.values_list('payment2', flat=True).get(custid=custid)
    l = g-k-k2
    m = Contract.objects.filter(custid=custid).update(finalpayment=l)
    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "m": m,
        "j": j,
    }
    return render(request, 'wsc/contract.html', context)


def thirddeposit(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_thirddeposit']
    f = Contract.objects.filter(custid=custid).update(payment3=d)
    a = JobCost.objects.values_list('grandtotalcost', flat=True).get(custid=custid)
    b = Contract.objects.values_list('deposit', flat=True).get(custid=custid)
    b2 = Contract.objects.values_list('payment2', flat=True).get(custid=custid)
    b3 = Contract.objects.values_list('payment3', flat=True).get(custid=custid)
    c = a-b-b2-b3
    g = Contract.objects.filter(custid=custid).update(finalpayment=c)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "g": g,

    }
    return render(request, 'wsc/contract.html', context)


def load_thirdamount(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    payment3a = a.values('payment3').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "payment3a": payment3a,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/third_payment.html', context)


def thirddp(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_pay3perc']
    f = Contract.objects.filter(custid=custid).update(pay3perc_id=d)
    g = JobCost.objects.values_list('grandtotalcost', flat=True).get(custid=custid)
    h = Contract.objects.values_list('pay3perc_id', flat=True).get(custid=custid)
    i = g * h
    j = Contract.objects.filter(custid=custid).update(payment3=i)
    k = Contract.objects.values_list('deposit', flat=True).get(custid=custid)
    k2 = Contract.objects.values_list('payment2', flat=True).get(custid=custid)
    k3 = Contract.objects.values_list('payment3', flat=True).get(custid=custid)
    l = g-k-k2-k3
    m = Contract.objects.filter(custid=custid).update(finalpayment=l)
    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "m": m,
        "j": j,
    }
    return render(request, 'wsc/contract.html', context)


def forthdeposit(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_forthdeposit']
    f = Contract.objects.filter(custid=custid).update(payment4=d)
    a = JobCost.objects.values_list('grandtotalcost', flat=True).get(custid=custid)
    b = Contract.objects.values_list('deposit', flat=True).get(custid=custid)
    b2 = Contract.objects.values_list('payment2', flat=True).get(custid=custid)
    b3 = Contract.objects.values_list('payment3', flat=True).get(custid=custid)
    b4 = Contract.objects.values_list('payment4', flat=True).get(custid=custid)
    c = a-b-b2-b3-b4
    g = Contract.objects.filter(custid=custid).update(finalpayment=c)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "g": g,

    }
    return render(request, 'wsc/contract.html', context)


def load_forthamount(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    payment4a = a.values('payment4').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "payment4a": payment4a,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/forth_payment.html', context)


def forthdp(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_pay4perc']
    f = Contract.objects.filter(custid=custid).update(pay4perc_id=d)
    g = JobCost.objects.values_list('grandtotalcost', flat=True).get(custid=custid)
    h = Contract.objects.values_list('pay4perc_id', flat=True).get(custid=custid)
    i = g * h
    j = Contract.objects.filter(custid=custid).update(payment4=i)
    k = Contract.objects.values_list('deposit', flat=True).get(custid=custid)
    k2 = Contract.objects.values_list('payment2', flat=True).get(custid=custid)
    k3 = Contract.objects.values_list('payment3', flat=True).get(custid=custid)
    k4 = Contract.objects.values_list('payment4', flat=True).get(custid=custid)
    l = g-k-k2-k3-k4
    m = Contract.objects.filter(custid=custid).update(finalpayment=l)
    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "m": m,
        "j": j,
    }
    return render(request, 'wsc/contract.html', context)


def load_finalpayment(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    finalpayment = a.values('finalpayment').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "finalpayment": finalpayment,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/final_payment.html', context)


def depositdate(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_depositdate']
    f = Contract.objects.filter(custid=custid).update(depositdate=d)
    context = {
        "instance": instance,
        "form": form,
        "f": f,
    }
    return render(request, 'wsc/contract.html', context)


def load_depositdate(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('depositdate').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute13_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/deposit_date.html', context)


def payment2date(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_payment2date']
    f = Contract.objects.filter(custid=custid).update(payment2date=d)
    context = {
        "instance": instance,
        "form": form,
        "f": f,
    }
    return render(request, 'wsc/contract.html', context)


def load_payment2date(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('payment2date').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute13_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/payment2_date.html', context)


def payment3date(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_payment3date']
    f = Contract.objects.filter(custid=custid).update(payment3date=d)
    context = {
        "instance": instance,
        "form": form,
        "f": f,
    }
    return render(request, 'wsc/contract.html', context)


def load_payment3date(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('payment3date').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute13_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/payment3_date.html', context)


def payment4date(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_payment4date']
    f = Contract.objects.filter(custid=custid).update(payment4date=d)
    context = {
        "instance": instance,
        "form": form,
        "f": f,
    }
    return render(request, 'wsc/contract.html', context)


def load_payment4date(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('payment4date').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute13_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/payment4_date.html', context)


def finalpaymentdate(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_finalpaymentdate']
    f = Contract.objects.filter(custid=custid).update(finalpaymentdate=d)
    context = {
        "instance": instance,
        "form": form,
        "f": f,
    }
    return render(request, 'wsc/contract.html', context)


def load_finalpaymentdate(request, custid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('finalpaymentdate').get(custid=custid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute13_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/finalpayment_date.html', context)

def installrate(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    t1 = JobCost.objects.values_list('totaljobcost', flat=True).get(custid=custid)
    t2 = JobCost.objects.values_list('construction', flat=True).get(custid=custid)
    t3 = JobCost.objects.values_list('opt2', flat=True).get(custid=custid)
    t4 = JobCost.objects.values_list('opt3', flat=True).get(custid=custid)
    t5 = JobCost.objects.values_list('installrate', flat=True).get(custid=custid)
    t6 = JobCost.objects.values_list('install_id', flat=True).get(custid=custid)
    t7 = t1 + t2 + t3 + t4 + t5
    t8 = t1 + t2 + t3 + t4
    if t6 == 2:
        JobCost.objects.filter(custid=custid).update(tax=0)
        JobCost.objects.filter(custid=custid).update(grandtotalcost=t8)
    elif t6 == 1:
        JobCost.objects.filter(custid=custid).update(installrate=t5)
        JobCost.objects.filter(custid=id).update(grandtotalcost=t7)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'wsc/contract.html', context)

def agreementlist(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_agreementlist']
    f = Agreement.objects.create(agreement=d)
    g = Agreement.objects.values_list('id', flat=True).last()
    h = Contract.objects.filter(custid=custid).update(memo1_id=g)
    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "h": h,
    }
    return render(request, 'wsc/contract.html', context)

def worktypelistdescr(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_worktypelistdescr']
    f = WorkType.objects.create(worktype=d)
    g = WorkType.objects.values_list('id', flat=True).last()
    h = Contract.objects.filter(custid=custid).update(worktype_id=g)
    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "h": h,
    }
    return render(request, 'wsc/contract.html', context)

def worktypedescr(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_worktypedescr']
    f = Ultimate.objects.create(ultimate=d)
    g = Ultimate.objects.values_list('id', flat=True).last()
    t2 = Contract.objects.values_list('memo2_id', flat=True).get(custid=custid)
    t3 = Contract.objects.values_list('memo3_id', flat=True).get(custid=custid)
    t4 = Contract.objects.values_list('memo4_id', flat=True).get(custid=custid)
    t5 = Contract.objects.values_list('memo5_id', flat=True).get(custid=custid)
    t6 = Contract.objects.values_list('memo6_id', flat=True).get(custid=custid)
    t7 = Contract.objects.values_list('memo7_id', flat=True).get(custid=custid)
    t8 = Contract.objects.values_list('memo8_id', flat=True).get(custid=custid)
    t9 = Contract.objects.values_list('memo9_id', flat=True).get(custid=custid)
    t10 = Contract.objects.values_list('memo10_id', flat=True).get(custid=custid)
    t11 = Contract.objects.values_list('memo11_id', flat=True).get(custid=custid)
    t12 = Contract.objects.values_list('memo12_id', flat=True).get(custid=custid)
    t13 = Contract.objects.values_list('memo13_id', flat=True).get(custid=custid)
    t14 = Contract.objects.values_list('memo14_id', flat=True).get(custid=custid)
    t15 = Contract.objects.values_list('memo15_id', flat=True).get(custid=custid)
    if t2 == 2:
        h = Contract.objects.filter(custid=custid).update(memo2_id=g)
    if t3 == 2:
        h = Contract.objects.filter(custid=custid).update(memo3_id=g)
    if t4 == 2:
        h = Contract.objects.filter(custid=custid).update(memo4_id=g)
    if t5 == 2:
        h = Contract.objects.filter(custid=custid).update(memo5_id=g)
    if t6 == 2:
        h = Contract.objects.filter(custid=custid).update(memo6_id=g)
    if t7 == 2:
        h = Contract.objects.filter(custid=custid).update(memo7_id=g)
    if t8 == 2:
        h = Contract.objects.filter(custid=custid).update(memo8_id=g)
    if t9 == 2:
        h = Contract.objects.filter(custid=custid).update(memo9_id=g)
    if t10 == 2:
        h = Contract.objects.filter(custid=custid).update(memo10_id=g)
    if t11 == 2:
        h = Contract.objects.filter(custid=custid).update(memo11_id=g)
    if t12 == 2:
        h = Contract.objects.filter(custid=custid).update(memo12_id=g)
    if t13 == 2:
        h = Contract.objects.filter(custid=custid).update(memo13_id=g)
    if t14 == 2:
        h = Contract.objects.filter(custid=custid).update(memo14_id=g)
    if t15 == 2:
        h = Contract.objects.filter(custid=custid).update(memo15_id=g)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "h": h,
    }
    return render(request, 'wsc/contract.html', context)

def includedescr(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_includedescr']
    f = Include.objects.create(include=d)
    g = Include.objects.values_list('id', flat=True).last()
    h = Contract.objects.filter(custid=custid).update(memo16_id=g)
    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "h": h,
    }
    return render(request, 'wsc/contract.html', context)

def excludedescr(request, custid=None):
    instance = Contract.objects.get(custid=custid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_excludedescr']
    f = Exclude.objects.create(exclude=d)
    g = Exclude.objects.values_list('id', flat=True).last()
    h = Contract.objects.filter(custid=custid).update(memo17_id=g)
    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "h": h,
    }
    return render(request, 'wsc/contract.html', context)
