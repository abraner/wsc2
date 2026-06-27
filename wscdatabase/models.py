from phone_field import PhoneField
from djmoney.models.fields import MoneyField
from django.utils.safestring import mark_safe
from django.db import models


class ContractorInfo(models.Model):
    objects = None
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    idA = models.IntegerField(null=True, default=None, verbose_name="Con. ID.")
    concompanytname = models.CharField(max_length=50, blank=True, verbose_name="Company Name:")
    confirstname = models.CharField(max_length=45, verbose_name="First Name:")
    conlastname = models.CharField(max_length=45, verbose_name="Last Name:")
    conadd1 = models.CharField(max_length=45, verbose_name="Address #1:")
    conadd2 = models.CharField(max_length=45, blank=True, verbose_name="Address #2:")
    concity = models.CharField(max_length=45, verbose_name="City:")
    const = models.CharField(max_length=2, verbose_name="St:")
    conzipcode = models.CharField(max_length=15, verbose_name="Zip Code:")
    conwork1 = PhoneField(blank=True, verbose_name="Work Phone #1:")
    conwork2 = PhoneField(blank=True, verbose_name="Work Phone #2:")
    concell1 = PhoneField(blank=True, verbose_name="Cell Phone #1:")
    concell2 = PhoneField(blank=True, verbose_name="Cell Phone #2:")
    conhome = PhoneField(blank=True, verbose_name="Home Phone:")
    conemail1 = models.EmailField(max_length=254, blank=True, verbose_name="Email #1:")
    conemail2 = models.EmailField(max_length=254, blank=True, verbose_name="Email #2:")

    class Meta:
        unique_together = ["confirstname", "conlastname", "conadd1", "concity", "const"]

    def get_absolute_url(self):
        return f"/wscdatabase/{self.id}/coninfo"

    def get_absolute8_url(self):
        return f"/wscdatabase/{self.id}/addcustconfirm/"

    def get_absolute29_url(self):
        return f"/wscdatabase/{self.id}/coninfo"

    def get_absolute36_url(self):
        return f"/wscdatabase/{self.id}/deletecontractor"

    def get_absolute37_url(self):
        return f"/wscdatabase/con_info_existing"


class ConDelete(models.Model):
    objects = None
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    conid = models.IntegerField(null=True, default=None, verbose_name="")


class ProdQueue(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    production = models.CharField(max_length=50, blank=True, unique=True, verbose_name="Production")
    increase = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=True, verbose_name="Increase / Decrease")

    def __str__(self):
        return str(self.production)


class CustomerInfo(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="Cust ID.")
    conid = models.IntegerField(null=True, default=None, verbose_name="Con. ID.")
    prodqueue = models.ForeignKey(ProdQueue, to_field="increase", related_name='prodqueue', null=True, blank=True,
                                default='0.00', on_delete=models.CASCADE, verbose_name="")
    custcompanytname = models.CharField(max_length=50, blank=True, verbose_name="Company Name:")
    custfirstname = models.CharField(max_length=45, verbose_name="First Name:")
    custlastname = models.CharField(max_length=45, verbose_name="Last Name:")
    custadd1 = models.CharField(max_length=45, verbose_name="Address #1:")
    custadd2 = models.CharField(max_length=45, blank=True, verbose_name="Address #2:")
    custcity = models.CharField(max_length=45, verbose_name="City:")
    custst = models.CharField(max_length=2, verbose_name="St:")
    custzipcode = models.CharField(max_length=15, verbose_name="Zip Code:")
    custwork1 = PhoneField(blank=True, verbose_name="Work Phone #1:")
    custwork2 = PhoneField(blank=True, verbose_name="Work Phone #2:")
    custcell1 = PhoneField(blank=True, verbose_name="Cell Phone #1:")
    custcell2 = PhoneField(blank=True, verbose_name="Cell Phone #2:")
    custhome = PhoneField(blank=True, verbose_name="Home Phone:")
    custemail1 = models.EmailField(max_length=254, blank=True, verbose_name="Email #1:")
    custemail2 = models.EmailField(max_length=254, blank=True, verbose_name="Email #2:")


    def get_absolute2_url(self):
        return f"/wscdatabase/{self.id}/dupconinfo/"

    def get_absolute3_url(self):
        return f"/wscdatabase/{self.id}/dupcustinfo/"

    def get_absolute4_url(self):
        return f"/wscdatabase/{self.id}/newcust"

    def get_absolute_url6(self):
        return f"/wscdatabase/{self.conid}/dupconinfo"

    def get_absolute5_url(self):
        return f"/wscdatabase/{self.id}/custinfo"

    def get_absolute7_url(self):
        return f"/wscdatabase/{self.id}/newcust/"

    def get_absolute9_url(self):
        return f"/wscdatabase/{self.id}/addcustconfirm/"

    def get_absolute10_url(self):
        return f"/wscdatabase/{self.id}/addcust/"

    def get_absolute25_url(self):
        return f"/wscdatabase/{self.id}/edit_cust_info/"

    def get_absolute26_url(self):
        return f"/wscdatabase/{self.id}/deletecust/"

    def get_absolute27_url(self):
        return f"/wscdatabase/cust_info_existing"

    def get_absolute28_url(self):
        return f"/wscdatabase/{self.conid}/coninfo"

    def get_absolute29_url(self):
        return f"/wscdatabase/con_info_existing"

    def get_absolute35_url(self):
        return f"/wscdatabase/{self.id}/prodconfirm"

    def get_absolute45_url(self):
        return f"/wscdatabase/{self.id}/deletecust2/"

    def get_absolute50_url(self):
        return f"/wscdatabase/{self.id}/jobcost/"


class Pricing(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    cabinet = models.IntegerField(null=True, default=None, verbose_name="Cabinets")
    cab_labor = models.IntegerField(null=True, default=None, verbose_name="Cabinet Labor")
    sides = models.IntegerField(null=True, default=None, verbose_name="Sides")
    drawer = models.IntegerField(null=True, default=None, verbose_name="Drawers")


class CabAcc(models.Model):
    cabacc_type = models.CharField(max_length=50, blank=True, unique=True, verbose_name="Cabinet Accessories")
    price = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="Price")

    def __str__(self):
        return str(self.cabacc_type)

    class Meta:
        db_table = 'wscdatabase_CabAcc'
        # Add verbose name
        verbose_name = 'Accessories'



class Comp(models.Model):
    comp_type = models.CharField(max_length=50, blank=True, unique=True, verbose_name="Cabinet Comp.")
    price = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="Price")
    labor = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="Comp. Labor")

    def __str__(self):
        return str(self.comp_type)

    class Meta:
        db_table = 'wscdatabase_Comp'
        # Add verbose name
        verbose_name = 'Cabinet Option'



class TaxRate(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    tax = models.CharField(max_length=50, blank=True, verbose_name="Tax Rate")
    taxperc = models.CharField(max_length=50, blank=True, verbose_name="")

    def __str__(self):
        return self.taxperc


class RoomType(models.Model):
    idA = models.IntegerField(null=True, default=None, verbose_name="")
    room_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.room_type


class NumType(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    num_type = models.IntegerField(null=True, default=None, unique=True, verbose_name="Cab. Num.")

    def __str__(self):
        return str(self.num_type)


class BidTbl(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    pageid = models.IntegerField(null=True, default=None, verbose_name="page ID.")
    bid_idA = models.IntegerField(null=True, default=None, verbose_name="bid ID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="Cust ID.")
    conid = models.IntegerField(null=True, default=None, verbose_name="Con. ID.")
    saleid = models.IntegerField(null=True, default=None, verbose_name="Sales ID.")
    max = models.IntegerField(null=True, default=None, verbose_name="")
    maxnum = models.IntegerField(null=True, default=None, verbose_name="")
    price = models.IntegerField(null=True, default=None, verbose_name="")
    custlastname = models.CharField(max_length=45, verbose_name="Last Name:")
    custadd1 = models.CharField(max_length=45, verbose_name="Address #1:")
    room = models.ForeignKey(RoomType, to_field="id", blank=True, null=True, default=None,
                             on_delete=models.CASCADE, verbose_name="Room")
    roomadd = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    roomadd2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    workorderdate = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True,
                                     verbose_name="Last Updated")
    date = models.DateField(auto_now_add=False, auto_now=True, blank=True, verbose_name="")
    totalroomlabor = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    cab1 = models.ForeignKey(NumType, to_field="num_type", related_name='cab1', null=True, blank=True, default=None,
                             on_delete=models.CASCADE, verbose_name="")
    cab1num = models.ForeignKey(NumType, to_field="num_type", related_name='cab1num', null=True, blank=True,
                                default=None, on_delete=models.CASCADE, verbose_name="")
    cab1sides = models.ForeignKey(NumType, to_field="num_type", related_name='cab1sides', null=True, blank=True,
                                  default=None, on_delete=models.CASCADE, verbose_name="")
    drwer1 = models.ForeignKey(NumType, to_field="num_type", related_name='drwer1', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Drawers")
    c11qty = models.ForeignKey(NumType, to_field="num_type", related_name='c11qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp11 = models.ForeignKey(Comp, to_field="id", related_name='comp11', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c12qty = models.ForeignKey(NumType, to_field="num_type", related_name='c12qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp12 = models.ForeignKey(Comp, to_field="id", related_name='comp12', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c13qty = models.ForeignKey(NumType, to_field="num_type", related_name='c13qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp13 = models.ForeignKey(CabAcc, to_field="id", related_name='comp13', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c14qty = models.ForeignKey(NumType, to_field="num_type", related_name='c14qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp14 = models.ForeignKey(CabAcc, to_field="id", related_name='comp14', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c15qty = models.ForeignKey(NumType, to_field="num_type", related_name='c15qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp15 = models.ForeignKey(CabAcc, to_field="id", related_name='comp15', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    cab2num = models.ForeignKey(NumType, to_field="num_type", related_name='cab2num', null=True, blank=True,
                                default=None, on_delete=models.CASCADE, verbose_name="")
    cab2 = models.ForeignKey(NumType, to_field="num_type", related_name='cab2', null=True, blank=True, default=None,
                             on_delete=models.CASCADE, verbose_name="")
    cab2sides = models.ForeignKey(NumType, to_field="num_type", related_name='cab2sides', null=True, blank=True,
                                  default=None, on_delete=models.CASCADE, verbose_name="")
    drwer2 = models.ForeignKey(NumType, to_field="num_type", related_name='drwer2', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Drawers")
    c21qty = models.ForeignKey(NumType, to_field="num_type", related_name='c21qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp21 = models.ForeignKey(Comp, to_field="id", related_name='comp21', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c22qty = models.ForeignKey(NumType, to_field="num_type", related_name='c22qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp22 = models.ForeignKey(Comp, to_field="id", related_name='comp22', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c23qty = models.ForeignKey(NumType, to_field="num_type", related_name='c23qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp23 = models.ForeignKey(CabAcc, to_field="id", related_name='comp23', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c24qty = models.ForeignKey(NumType, to_field="num_type", related_name='c24qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp24 = models.ForeignKey(CabAcc, to_field="id", related_name='comp24', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c25qty = models.ForeignKey(NumType, to_field="num_type", related_name='c25qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp25 = models.ForeignKey(CabAcc, to_field="id", related_name='comp25', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    cab3num = models.ForeignKey(NumType, to_field="num_type", related_name='cab3num', null=True, blank=True,
                                default=None, on_delete=models.CASCADE, verbose_name="")
    cab3 = models.ForeignKey(NumType, to_field="num_type", related_name='cab3', null=True, blank=True, default=None,
                             on_delete=models.CASCADE, verbose_name="")
    cab3sides = models.ForeignKey(NumType, to_field="num_type", related_name='cab3sides', null=True, blank=True,
                                  default=None, on_delete=models.CASCADE, verbose_name="")
    drwer3 = models.ForeignKey(NumType, to_field="num_type", related_name='drwer3', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Drawers")
    c31qty = models.ForeignKey(NumType, to_field="num_type", related_name='c31qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp31 = models.ForeignKey(Comp, to_field="id", related_name='comp31', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c32qty = models.ForeignKey(NumType, to_field="num_type", related_name='c32qty32', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    comp32 =  models.ForeignKey(Comp, to_field="id", related_name='comp32', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c33qty = models.ForeignKey(NumType, to_field="num_type", related_name='c33qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp33 = models.ForeignKey(CabAcc, to_field="id", related_name='comp33', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c34qty = models.ForeignKey(NumType, to_field="num_type", related_name='c34qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp34 = models.ForeignKey(CabAcc, to_field="id", related_name='comp34', null=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c35qty = models.ForeignKey(NumType, to_field="num_type", related_name='c35qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp35 = models.ForeignKey(CabAcc, to_field="id", related_name='comp35', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    rmactive = models.IntegerField(null=True, default=None, verbose_name="")


    def get_absolute11_url(self):
        return f"/wscdatabase/{self.id}/bidpage"

    def get_absolute_url12(self):
        return f"/wscdatabase/{self.bid_idA}/bidpage"

    def get_absolute_url13(self):
        return f"/wscdatabase/{self.bid_idA}/addnewrm"

    def get_absolute14_url(self):
        return f"/wscdatabase/{self.bid_idA}/changermnum"

    def get_absolute15_url(self):
        return f"/wscdatabase/{self.id}/changermnum"

    def get_absolute19_url(self):
        return f"/wscdatabase/{self.custid}/custinfo"


class BidTbl2(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    idA = models.IntegerField(null=True, default=None, verbose_name="page ID.")
    pageid = models.IntegerField(null=True, default=None, verbose_name="page ID.")
    bid_idA = models.IntegerField(null=True, default=None, verbose_name="bid ID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="Cust ID.")
    conid = models.IntegerField(null=True, default=None, verbose_name="Con. ID.")
    saleid = models.IntegerField(null=True, default=None, verbose_name="Sales ID.")
    price = models.IntegerField(null=True, default=None, verbose_name="")
    cab4num = models.ForeignKey(NumType, to_field="num_type", related_name='cab4num', null=True, blank=True,
                                default=None, on_delete=models.CASCADE, verbose_name="")
    cab4 = models.ForeignKey(NumType, to_field="num_type", related_name='cab4', null=True, default=None,
                             on_delete=models.CASCADE, verbose_name="")
    cab4sides = models.ForeignKey(NumType, to_field="num_type", related_name='cab4sides', null=True, blank=True,
                                  default=None, on_delete=models.CASCADE, verbose_name="")
    drwer4 = models.ForeignKey(NumType, to_field="num_type", related_name='drwer4', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Drawers")
    c41qty = models.ForeignKey(NumType, to_field="num_type", related_name='c41qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp41 = models.ForeignKey(Comp, to_field="id", related_name='comp41', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c42qty = models.ForeignKey(NumType, to_field="num_type", related_name='c42qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp42 = models.ForeignKey(Comp, to_field="id", related_name='comp42', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c43qty = models.ForeignKey(NumType, to_field="num_type", related_name='c43qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp43 = models.ForeignKey(CabAcc, to_field="id", related_name='comp43', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c44qty = models.ForeignKey(NumType, to_field="num_type", related_name='c44qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp44 = models.ForeignKey(CabAcc, to_field="id", related_name='comp44', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c45qty = models.ForeignKey(NumType, to_field="num_type", related_name='c45qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp45 = models.ForeignKey(CabAcc, to_field="id", related_name='comp45', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    cab5num = models.ForeignKey(NumType, to_field="num_type", related_name='cab5num', null=True, blank=True,
                                default=None, on_delete=models.CASCADE, verbose_name="")
    cab5 = models.ForeignKey(NumType, to_field="num_type", related_name='cab5', blank=True, null=True, default=None,
                             on_delete=models.CASCADE, verbose_name="")
    cab5sides = models.ForeignKey(NumType, to_field="num_type", related_name='cab5sides', null=True, blank=True,
                                  default=None, on_delete=models.CASCADE, verbose_name="")
    drwer5 = models.ForeignKey(NumType, to_field="num_type", related_name='drwer5', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Drawers")
    c51qty = models.ForeignKey(NumType, to_field="num_type", related_name='c51qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp51 = models.ForeignKey(Comp, to_field="id", related_name='comp51', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c52qty = models.ForeignKey(NumType, to_field="num_type", related_name='c52qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp52 = models.ForeignKey(Comp, to_field="id", related_name='comp52', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c53qty = models.ForeignKey(NumType, to_field="num_type", related_name='c53qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp53 = models.ForeignKey(CabAcc, to_field="id", related_name='comp53', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c54qty = models.ForeignKey(NumType, to_field="num_type", related_name='c54qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp54 = models.ForeignKey(CabAcc, to_field="id", related_name='comp54', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c55qty = models.ForeignKey(NumType, to_field="num_type", related_name='c55qty',null=True,  blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp55 = models.ForeignKey(CabAcc, to_field="id", related_name='comp55', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    cab6num = models.ForeignKey(NumType, to_field="num_type", related_name='cab6num', null=True, blank=True,
                                default=None, on_delete=models.CASCADE, verbose_name="")
    cab6 = models.ForeignKey(NumType, to_field="num_type", related_name='cab6', null=True, blank=True, default=None,
                             on_delete=models.CASCADE, verbose_name="")
    cab6sides = models.ForeignKey(NumType, to_field="num_type", related_name='cab6sides', null=True, blank=True,
                                  default=None, on_delete=models.CASCADE, verbose_name="")
    drwer6 = models.ForeignKey(NumType, to_field="num_type", related_name='drwer6', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Drawers")
    c61qty = models.ForeignKey(NumType, to_field="num_type", related_name='c61qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp61 = models.ForeignKey(Comp, to_field="id", related_name='comp61', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c62qty = models.ForeignKey(NumType, to_field="num_type", related_name='c62qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp62 = models.ForeignKey(Comp, to_field="id", related_name='comp62', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c63qty = models.ForeignKey(NumType, to_field="num_type", related_name='c63qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp63 = models.ForeignKey(CabAcc, to_field="id", related_name='comp63', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c64qty = models.ForeignKey(NumType, to_field="num_type", related_name='c64qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp64 = models.ForeignKey(CabAcc, to_field="id", related_name='comp64', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    c65qty = models.ForeignKey(NumType, to_field="num_type", related_name='c65qty', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Qty")
    comp65 = models.ForeignKey(CabAcc, to_field="id", related_name='comp65', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")

    def get_absolute_url11(self):
        return f"/wscdatabase/{self.id}/bidpage"


class CurrentRm(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    rm_idA = models.IntegerField(null=True, default=None, verbose_name="Room ID.")
    bid_idA = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="Cust ID.")
    conid = models.IntegerField(null=True, default=None, verbose_name="Con. ID.")
    saleid = models.IntegerField(null=True, default=None, verbose_name="Sales ID.")
    rmnum = models.ForeignKey(RoomType, to_field="id", related_name='rmnum', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Room")
    rmcost = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null=True, blank=True, default='0.00', verbose_name="Room Cost")
    rmactive = models.BooleanField(verbose_name="Room Active", default=True)
    rmdelete = models.BooleanField(verbose_name="Delete Room", default=False)


    def get_absolute16_url(self):
        return f"/wscdatabase/{self.bid_idA}/bidpage"

    def get_absolute17_url(self):
        return f"/wscdatabase/{self.bid_idA}/rmselection"

    def get_absolute18_url(self):
        return f"/wscdatabase/{self.bid_idA}/totalrmcost"

    def get_absolute180_url(self):
        return f"/wscdatabase/{self.bid_idA}/totalrmcost2"

    def get_absolute20_url(self):
        return f"/wscdatabase/{self.bid_idA}/addtocontract"

    def get_absolute22_url(self):
        return f"/wscdatabase/{self.bid_idA}/deleterm"

    def get_absolute23_url(self):
        return f"/wscdatabase/{self.bid_idA}/deleterm1"

    def get_absolute24_url(self):
        return f"/wscdatabase/{self.custid}/custinfo"


class Ultimate(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    ultimate = models.CharField(max_length=150, blank=True, verbose_name="")

    def __str__(self):
        return str(self.ultimate)

    class Meta:
        db_table = 'wscdatabase_Ultimate'
        # Add verbose name
        verbose_name = 'Work Type List'




class WorkType(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    worktype = models.CharField(max_length=150, blank=True, verbose_name="")

    def __str__(self):
        return str(self.worktype)

    class Meta:
        db_table = 'wscdatabase_WorkType'
        # Add verbose name
        verbose_name = 'Work Type'

class WoodSpecies(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    woodspecies = models.CharField(max_length=50, blank=True, verbose_name="Wood Species")
    increase = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Increase")

    def __str__(self):
        return str(self.woodspecies)

    class Meta:
        db_table = 'wscdatabase_WoodSpecies'
        # Add verbose name
        verbose_name = 'Wood Specie'



class DoorStyle(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    doorstyle = models.CharField(max_length=50, blank=True, verbose_name="Door Style")
    increase = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Increase")

    def __str__(self):
        return str(self.doorstyle)


class FinishColor(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    finishcolor = models.CharField(max_length=50, blank=True, verbose_name="Finish Color")
    increase = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Increase")

    def __str__(self):
        return str(self.finishcolor)


class FinishOption(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    finishoption = models.CharField(max_length=50, blank=True, verbose_name="Finish Option")
    increase = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Increase")

    def __str__(self):
        return str(self.finishoption)


class TotalRoomCost(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    bid_idA = models.IntegerField(null=True, default=None, verbose_name="bid ID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="Cust ID.")
    conid = models.IntegerField(null=True, default=None, verbose_name="Con. ID.")
    saleid = models.IntegerField(null=True, default=None, verbose_name="Sales ID.")
    room = models.ForeignKey(RoomType, to_field="id", related_name='comp24', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Room")
    rmname = models.CharField(max_length=45, verbose_name="Address #1:")
    rmactive = models.IntegerField(null=True, default=None, verbose_name="")
    custlastname = models.CharField(max_length=45, verbose_name="Last Name:")
    custadd1 = models.CharField(max_length=45, verbose_name="Address #1:")
    cabnumtotal = models.IntegerField(null=True, default='0', verbose_name="Number of Cabinets")
    cabinet = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null=True, blank=True, default='0.00',
                         verbose_name="Cabinet Cost")
    cabtotalprice = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null=True, blank=True, default='0.00',
                               verbose_name="Price for Cabinets")
    cabsidenum = models.IntegerField(null=True, default='0', verbose_name="Number of Sides")
    cabsidecost = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null=True, blank=True, default='0.00',
                             verbose_name="Side Cost")
    cabsidetotal = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null=True, blank=True, default='0.00',
                              verbose_name="Price for Sides")
    drawernum = models.IntegerField(null=True, default='0', verbose_name="Number of Drawers")
    drawercost = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null=True, blank=True, default='0.00',
                            verbose_name="Drawer Cost")
    drawertotal = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null=True, blank=True, default='0.00',
                             verbose_name="Price for Drawers")
    optionnum = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null=True, blank=True, default='0.00',
                           verbose_name="Cabinet Options")
    custcabcost = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null=True, blank=True, default='0.00',
                             verbose_name="Custom Cost")
    custcabtotal = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null=True, blank=True, default='0.00',
                              verbose_name="Custom Cabinet Total")
    custsidecost = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null=True, blank=True, default='0.00',
                              verbose_name="Custom Cost")
    custsidetotal = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null=True, blank=True, default='0.00',
                               verbose_name="Custom Sides Total")
    cabaccrmtotal = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null=True, blank=True, default='0.00',
                               verbose_name="Cabinet Accessories")
    cabacccustom = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null=True, blank=True, default='0.00',
                              verbose_name="Custom Cost")
    cabacctotal = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null=True, blank=True, default='0.00',
                             verbose_name="Custom Cabinet Acc.Total")
    totalrmcost = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null=True, blank=True, default='0.00',
                             verbose_name="Total Room Cost")
    prodqueuetotal = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null=True, blank=True,
                             default='0.00',
                             verbose_name="Production Queue Total")
    rmgrandtotal = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null=True, blank=True,
                             default='0.00',
                             verbose_name="Room Grand Total")
    woodspecies = models.ForeignKey(WoodSpecies, to_field="id", related_name='comp24', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Wood Species")
    wood = models.CharField(max_length=45, null=True, blank=True, verbose_name="Address #1:")
    woodspeciesperc = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="")
    doorstyle = models.ForeignKey(DoorStyle, to_field="id", related_name='comp24', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Door Style")
    door = models.CharField(max_length=45, null=True, blank=True, verbose_name="Address #1:")
    doorstyleperc = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="")
    finishcolor = models.ForeignKey(FinishColor, to_field="id", related_name='comp24', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Finish Color")
    fncolor = models.CharField(max_length=45, null=True, blank=True, verbose_name="Address #1:")
    finishcolorperc = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="")
    finishoption1 = models.ForeignKey(FinishOption, to_field="id", related_name='comp24', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Finish Option")
    fnoption = models.CharField(max_length=45, null=True, blank=True, verbose_name="Address #1:")
    finishoption2perc = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="")
    finishoption2 = models.ForeignKey(FinishOption, to_field="id", related_name='comp25', null=True, blank=True,
                                      default=None, on_delete=models.CASCADE, verbose_name="Finish Option")
    fnoption2 = models.CharField(max_length=45, null=True, blank=True, verbose_name="Address #1:")
    finishoption1perc = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="")
    totalperc = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="Total Percentage Increase")
    totallabor = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")


    def get_totalrmcost(self, obj):
        return mark_safe('&USD;{}'.format(obj.totalrmcost))

    def get_absolute11_url(self):
        return f"/wscdatabase/{self.id}/bidpage"

    def get_absolute13_url(self):
        return f"/wscdatabase/{self.bid_idA}/totalrmcost"

    def get_absolute21_url(self):
        return f"/wscdatabase/{self.custid}/custinfo"

    def get_absolute22_url(self):
        return f"/wscdatabase/con_info_existing"


class Cabinet(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    bid_idA = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    conid = models.IntegerField(null=True, default=None, verbose_name="")
    saleid = models.IntegerField(null=True, default=None, verbose_name="")
    jobid = models.IntegerField(null=True, default=None, verbose_name="")
    roomid = models.IntegerField(null=True, default=None, verbose_name="")
    cabqty = models.IntegerField(null=True, default=None, verbose_name="")
    cablabor = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    totalcablabor = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")


class CabSide(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    bidid = models.IntegerField(null=True, default=None, verbose_name="")
    bid_idA = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    conid = models.IntegerField(null=True, default=None, verbose_name="")
    saleid = models.IntegerField(null=True, default=None, verbose_name="")
    ident = models.IntegerField(null=True, default=None, verbose_name="")
    cabsideqty = models.IntegerField(null=True, default=None, verbose_name="")


class Drawer(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    bidid = models.IntegerField(null=True, default=None, verbose_name="")
    bid_idA = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    conid = models.IntegerField(null=True, default=None, verbose_name="")
    saleid = models.IntegerField(null=True, default=None, verbose_name="")
    ident = models.IntegerField(null=True, default=None, verbose_name="")
    drawerqty = models.IntegerField(null=True, default=None, verbose_name="")


class AccOption(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    idA = models.IntegerField(null=True, default=None, verbose_name="")
    pageid = models.IntegerField(null=True, default=None, verbose_name="")
    bidid = models.IntegerField(null=True, default=None, verbose_name="")
    bid_idA = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    conid = models.IntegerField(null=True, default=None, verbose_name="")
    saleid = models.IntegerField(null=True, default=None, verbose_name="")
    roomid = models.IntegerField(null=True, default=None, verbose_name="")
    ident = models.IntegerField(null=True, default=None, verbose_name="")
    accqty = models.IntegerField(null=True, default=None, verbose_name="")
    acc = models.IntegerField(null=True, default=None, verbose_name="")
    accname = models.CharField(max_length=50, blank=True, verbose_name="")
    price = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    totalprice = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")


class CompOption(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    idA = models.IntegerField(null=True, default=None, verbose_name="")
    pageid = models.IntegerField(null=True, default=None, verbose_name="")
    bidid = models.IntegerField(null=True, default=None, verbose_name="")
    bid_idA = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    conid = models.IntegerField(null=True, default=None, verbose_name="")
    saleid = models.IntegerField(null=True, default=None, verbose_name="")
    roomid = models.IntegerField(null=True, default=None, verbose_name="")
    ident = models.IntegerField(null=True, default=None, verbose_name="")
    compqty = models.IntegerField(null=True, default=None, verbose_name="")
    comp = models.IntegerField(null=True, default=None, verbose_name="")
    compname = models.CharField(max_length=45, null=True, verbose_name="")
    price = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    totalprice = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    labor = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    totallabor = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")


class CompOptionTotal(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    bidid = models.IntegerField(null=True, default=None, verbose_name="")
    bid_idA = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    conid = models.IntegerField(null=True, default=None, verbose_name="")
    saleid = models.IntegerField(null=True, default=None, verbose_name="")
    jobid = models.IntegerField(null=True, default=None, verbose_name="")
    roomid = models.IntegerField(null=True, default=None, verbose_name="")
    compqty = models.IntegerField(null=True, default=None, verbose_name="")
    comp = models.IntegerField(null=True, default=None, verbose_name="")
    compname = models.CharField(max_length=50, blank=True, verbose_name="")
    price = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    totalprice = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    labor = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    totallabor = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")


class AccOptionTotal(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    bidid = models.IntegerField(null=True, default=None, verbose_name="")
    bid_idA = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    conid = models.IntegerField(null=True, default=None, verbose_name="")
    saleid = models.IntegerField(null=True, default=None, verbose_name="")
    roomid = models.IntegerField(null=True, default=None, verbose_name="")
    total_qty = models.IntegerField(null=True, default=None, verbose_name="")
    acc = models.IntegerField(null=True, default=None, verbose_name="")
    accname = models.CharField(max_length=50, blank=True, verbose_name="")
    price = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    totalprice = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")


class Totals(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    bid_idA = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    conid = models.IntegerField(null=True, default=None, verbose_name="")
    saleid = models.IntegerField(null=True, default=None, verbose_name="")
    rmcost = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="Room Cost")
    totalrmcost = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="Total Room Cost")
    increase = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="Increase")
    totalincrease = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    optionnum = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    optionnumincrease = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    optionnumtotal = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    cabaccrmtotal = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    cabaccrmtotalincrease = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    cabaccrmtotaltotal = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    baseprice = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")


class DeleteRm(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    deleterm = models.IntegerField(null=True, default=None, verbose_name="")

    def get_absolute36_url(self):
        return f"/wscdatabase/{self.deleterm}/custinfo"


class DeleteCust(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    deletecust = models.IntegerField(null=True, default=None, verbose_name="")
    deletecon = models.IntegerField(null=True, default=None, verbose_name="")

    def get_absolute_url(self):
        return f"/wscdatabase/{self.deletecust}/coninfo"


class Labor(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    jobid = models.IntegerField(null=True, default=None, verbose_name="")
    bid_idA = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    conid = models.IntegerField(null=True, default=None, verbose_name="")
    room = models.IntegerField(null=True, default=None, verbose_name="")
    labor = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    rmactive = models.IntegerField(null=True, default=None, verbose_name="")


class ContractOption(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    conoption = models.CharField(max_length=50, blank=True, verbose_name="Contract Option")

    def __str__(self):
        return str(self.conoption)


class YesNo(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    yesno = models.CharField(max_length=50, blank=True, verbose_name="Contract Option")

    def __str__(self):
        return str(self.yesno)


class JobCost(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    jobid = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    conid = models.IntegerField(null=True, default=None, verbose_name="")
    saleid = models.IntegerField(null=True, default=None, verbose_name="")
    custlastname = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="Last Name:")
    custadd1 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="Address #1:")
    totalrmcost = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="Cabinetry")
    customtext = models.ForeignKey(ContractOption, to_field="id", related_name='customtext', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Custom Text")
    custom = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    discounttext = models.ForeignKey(ContractOption, to_field="id", related_name='discounttext', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Discount Text")
    discount = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    subtotalcost = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="Sub Total Cost")
    tax = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="Tax")
    taxrate = models.DecimalField(decimal_places=4, max_digits=7, default='0.0000', verbose_name="Tax Rate")
    totaljobcost = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="Total Job Cost")
    constructiontext = models.ForeignKey(ContractOption, to_field="id", related_name='constructiontext', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Construction Text")
    construction = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    opt2text = models.ForeignKey(ContractOption, to_field="id", related_name='opt2text', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="opt2text")
    opt2 = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    opt3text =models.ForeignKey(ContractOption, to_field="id", related_name='opt3text', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="opt3text")
    opt3 = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    install = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    installrate = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="Install")
    grandtotalcost = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="Grand Total Cost")

    installtext = models.ForeignKey(YesNo, to_field="id", related_name='install', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="Construction Text")
    customamount = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    discountamount = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    constructionamount = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    opt2amount = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    opt3amount = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")

    def get_absolute_url(self):
        return f"/wscdatabase/{self.custid}/jobcost"


class LaborBd(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    jobid = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    room = models.IntegerField(null=True, default=None, verbose_name="")


class Percentage(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    percent = models.CharField(max_length=50, blank=True, verbose_name="")
    multiplier = models.DecimalField(decimal_places=2, unique=True, max_digits=7, default='0.00', verbose_name="")

    def __str__(self):
        return str(self.percent)


class Agreement(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    agreement = models.CharField(max_length=150, blank=True, verbose_name="")

    def __str__(self):
        return str(self.agreement)


class Terms(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    terms = models.CharField(max_length=150, blank=True, verbose_name="")

    def __str__(self):
        return str(self.terms)


class Include(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    include = models.CharField(max_length=250, blank=True, verbose_name="")

    def __str__(self):
        return str(self.include)


class Exclude(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    exclude = models.CharField(max_length=250, blank=True, verbose_name="")

    def __str__(self):
        return str(self.exclude)






class Contract(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    jobid = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    conid = models.IntegerField(null=True, default=None, verbose_name="")
    workorderdate = models.DateField(blank=True, null=True)
    date = models.DateField(auto_now_add=False, auto_now=True, blank=True)
    totalrmcost = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    custom = models.IntegerField(null=True, default=None, verbose_name="")
    customtext = models.IntegerField(null=True, default=None, verbose_name="")
    construction = models.IntegerField(null=True, default=None, verbose_name="")
    constructiontext = models.IntegerField(null=True, default=None, verbose_name="")
    install = models.IntegerField(null=True, default=None, verbose_name="")
    discount = models.IntegerField(null=True, default=None, verbose_name="")
    discounttext = models.IntegerField(null=True, default=None, verbose_name="")
    opt1num = models.IntegerField(null=True, default=None, verbose_name="")
    opt1text = models.IntegerField(null=True, default=None, verbose_name="")
    opt2num = models.IntegerField(null=True, default=None, verbose_name="")
    opt2text = models.IntegerField(null=True, default=None, verbose_name="")
    opt3num = models.IntegerField(null=True, default=None, verbose_name="")
    opt3text = models.IntegerField(null=True, default=None, verbose_name="")
    taxrate = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    tax = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    subtotalcost = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    totaljobcost = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    grandtotalcost = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    worktype = models.ForeignKey(WorkType, to_field="id", related_name='worktype1', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    memo1 = models.ForeignKey(Agreement, to_field="id", related_name='memo1', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    memo2 = models.ForeignKey(Ultimate, to_field="id", related_name='memo2', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    memo3 = models.ForeignKey(Ultimate, to_field="id", related_name='memo3', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    memo4 = models.ForeignKey(Ultimate, to_field="id", related_name='memo4', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    memo5 = models.ForeignKey(Ultimate, to_field="id", related_name='memo5', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    memo6 = models.ForeignKey(Ultimate, to_field="id", related_name='memo6', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    memo7 = models.ForeignKey(Ultimate, to_field="id", related_name='memo7', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    memo8 = models.ForeignKey(Ultimate, to_field="id", related_name='memo8', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    memo9 = models.ForeignKey(Ultimate, to_field="id", related_name='memo9', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    memo10 = models.ForeignKey(Ultimate, to_field="id", related_name='memo10', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    memo11 = models.ForeignKey(Ultimate, to_field="id", related_name='memo11', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    memo12 = models.ForeignKey(Ultimate, to_field="id", related_name='memo12', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    memo13 = models.ForeignKey(Ultimate, to_field="id", related_name='memo13', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    memo14 = models.ForeignKey(Ultimate, to_field="id", related_name='memo14', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    memo15 = models.ForeignKey(Ultimate, to_field="id", related_name='memo15', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    memo16 = models.ForeignKey(Include, to_field="id", related_name='memo16', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    memo17 = models.ForeignKey(Exclude, to_field="id", related_name='memo17', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    depositperc = models.ForeignKey(Percentage, to_field="multiplier", related_name='depositperc', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    depositterms = models.ForeignKey(Terms, to_field="id", related_name='term', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    deposit = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    depositdate = models.DateField(blank=True, null=True)
    pay2perc = models.ForeignKey(Percentage, to_field="multiplier", related_name='pay2perc', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    payment2 = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    terms2 = models.ForeignKey(Terms, to_field="id", related_name='term2', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    payment2date = models.DateField(blank=True, null=True)
    pay3perc = models.ForeignKey(Percentage, to_field="multiplier", related_name='pay3perc', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    terms3 = models.ForeignKey(Terms, to_field="id", related_name='term3', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    payment3 = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    payment3date = models.DateField(blank=True, null=True)
    pay4perc = models.ForeignKey(Percentage, to_field="multiplier", related_name='pay4perc', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    terms4 = models.ForeignKey(Terms, to_field="id", related_name='term4', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    payment4 = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    payment4date = models.DateField(blank=True, null=True)
    finalperc = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    termsfinal = models.ForeignKey(Terms, to_field="id", related_name='termfinal', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    finalpayment = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    finalpaymentdate = models.DateField(blank=True, null=True)
    customdeposit = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    seconddeposit = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    thirddeposit = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    forthdeposit = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    agreementlist = models.CharField(max_length=250, blank=True, verbose_name="")
    worktypelistdescr = models.CharField(max_length=250, blank=True, verbose_name="")
    worktypedescr = models.CharField(max_length=250, blank=True, verbose_name="")
    excludedescr = models.CharField(max_length=250, blank=True, verbose_name="")
    includedescr = models.CharField(max_length=250, blank=True, verbose_name="")

    def get_absolute_url(self):
        return f"/wscdatabase/{self.custid}/contract"


class IncludedOption(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    conid = models.IntegerField(null=True, default=None, verbose_name="")
    compqty = models.IntegerField(null=True, default=None, verbose_name="")
    comp = models.IntegerField(null=True, default=None, verbose_name="")
    compname = models.CharField(max_length=150, blank=True, verbose_name="")


class IncludedAcc(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    conid = models.IntegerField(null=True, default=None, verbose_name="")
    accqty = models.IntegerField(null=True, default=None, verbose_name="")
    acc = models.IntegerField(null=True, default=None, verbose_name="")
    accname = models.CharField(max_length=150, blank=True, verbose_name="")


class ContractInclude(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    idA = models.IntegerField(null=True, default=None, verbose_name="")
    bid_idA = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    conid = models.IntegerField(null=True, default=None, verbose_name="")
    pageid = models.IntegerField(null=True, default=None, verbose_name="")
    ident = models.IntegerField(null=True, default=None, verbose_name="")
    rmactive = models.IntegerField(null=True, default=None, verbose_name="")
    qty = models.IntegerField(null=True, default=None, verbose_name="")
    includeid = models.IntegerField(null=True, default=None, verbose_name="")
    name = models.CharField(max_length=150, blank=True, verbose_name="")


class ContractIncludeTotal(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    bid_idA = models.IntegerField(null=True, default=None, verbose_name="")
    bidid = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    conid = models.IntegerField(null=True, default=None, verbose_name="")
    includeid = models.IntegerField(null=True, default=None, verbose_name="")
    qty = models.IntegerField(null=True, default=None, verbose_name="")
    name = models.CharField(max_length=150, blank=True, verbose_name="")
    rmactive = models.IntegerField(null=True, default=None, verbose_name="")


class Legally1(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    legal = models.CharField(max_length=150, blank=True, verbose_name="")


class Legally2(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    legal = models.CharField(max_length=150, blank=True, verbose_name="")


class Legally3(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    legal = models.CharField(max_length=150, blank=True, verbose_name="")


class Legally4(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    legal = models.CharField(max_length=150, blank=True, verbose_name="")


class Legally5(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    legal = models.TextField(blank=True, verbose_name="")
