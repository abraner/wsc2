from django import forms
from .models import CustomerInfo, ContractorInfo, CurrentRm, BidTbl, BidTbl2, TotalRoomCost, RoomType, JobCost, \
                    CompOptionTotal, Cabinet, Contract


class Coninfo(forms.ModelForm):
    class Meta:
        model = ContractorInfo
        fields = [
            'concompanytname',
            'confirstname',
            'conlastname',
            'conadd1',
            'conadd2',
            'concity',
            'const',
            'conzipcode',
            'conwork1',
            'conwork2',
            'concell1',
            'concell2',
            'conhome',
            'conemail1',
            'conemail2',
        ]

        widgets = {'conwork1': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'conwork2': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'concell1': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'concell2': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'conhome': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   }

class ConinfoA(forms.ModelForm):
    class Meta:
        model = ContractorInfo
        fields = [
            'id',
            'idA',
            'concompanytname',
            'confirstname',
            'conlastname',
            'conadd1',
            'conadd2',
            'concity',
            'const',
            'conzipcode',
            'conwork1',
            'conwork2',
            'concell1',
            'concell2',
            'conhome',
            'conemail1',
            'conemail2',
        ]

        widgets = {'conwork1': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'conwork2': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'concell1': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'concell2': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'conhome': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   }


class DupConInfo(forms.ModelForm):

    class Meta:
        model = CustomerInfo
        fields = [
            'custid',
            'conid',
        ]


class RmSelection(forms.ModelForm):

    class Meta:
        model = CurrentRm
        fields = [
            'bid_idA',
            'custid',
        ]


class BidPageSelection(forms.ModelForm):

    class Meta:
        model = BidTbl
        fields = [
            'bid_idA',
            'custid',
        ]


class AddCustConfirm(forms.ModelForm):

    class Meta:
        model = CustomerInfo
        fields = [
            'custid',
        ]


class Custinfo(forms.ModelForm):

    class Meta:
        model = CustomerInfo
        fields = [
            'custid',
            'conid',
            'custcompanytname',
            'custfirstname',
            'custlastname',
            'custadd1',
            'custadd2',
            'custcity',
            'custst',
            'custzipcode',
            'custwork1',
            'custwork2',
            'custcell1',
            'custcell2',
            'custhome',
            'custemail1',
            'custemail2'
        ]

        widgets = {'custwork1': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custwork2': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custcell1': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custcell2': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custhome': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   }



class CustinfoB(forms.ModelForm):

    class Meta:
        model = CustomerInfo
        fields = [
            'custid',
            'conid',
            'prodqueue',
            'custcompanytname',
            'custfirstname',
            'custlastname',
            'custadd1',
            'custadd2',
            'custcity',
            'custst',
            'custzipcode',
            'custwork1',
            'custwork2',
            'custcell1',
            'custcell2',
            'custhome',
            'custemail1',
            'custemail2'
        ]
        widgets = {'custwork1': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custwork2': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custcell1': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custcell2': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custhome': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   }



class CustinfoA(forms.ModelForm):

    class Meta:
        model = CustomerInfo
        fields = [
            'custid',
            'custcompanytname',
            'custfirstname',
            'custlastname',
            'custadd1',
            'custadd2',
            'custcity',
            'custst',
        ]


class CustinfoC(forms.ModelForm):

    class Meta:
        model = CustomerInfo
        fields = [
            'custcompanytname',
            'custfirstname',
            'custlastname',
            'custadd1',
            'custadd2',
            'custcity',
            'custst',
            'custzipcode',
            'custwork1',
            'custwork2',
            'custcell1',
            'custcell2',
            'custhome',
            'custemail1',
            'custemail2'
        ]

        widgets = {'custwork1': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custwork2': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custcell1': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custcell2': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custhome': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   }


class CurrRm(forms.ModelForm):
    class Meta:
        model = CurrentRm
        fields = [
            'rm_idA',
            'bid_idA',
            'rmnum',
            'rmcost',
            'rmactive',
            'rmdelete',
            'custid',

        ]


class BidPage(forms.ModelForm):
    class Meta:
        model = BidTbl
        fields = [
            'bid_idA',
            'pageid',
            'custid',
            'conid',
            'saleid',
            'max',
            'maxnum',
            'price',
            'custlastname',
            'custadd1',
            'room',
            'roomadd',
            'roomadd2',
            'cab1num',
            'cab1',
            'cab1sides',
            'drwer1',
            'c11qty',
            'comp11',
            'c12qty',
            'comp12',
            'c13qty',
            'comp13',
            'c14qty',
            'comp14',
            'c15qty',
            'comp15',
            'cab2num',
            'cab2',
            'cab2sides',
            'drwer2',
            'c21qty',
            'comp21',
            'c22qty',
            'comp22',
            'c23qty',
            'comp23',
            'c24qty',
            'comp24',
            'c25qty',
            'comp25',
            'cab3num',
            'cab3',
            'cab3sides',
            'drwer3',
            'c31qty',
            'comp31',
            'c32qty',
            'comp32',
            'c33qty',
            'comp33',
            'c34qty',
            'comp34',
            'c35qty',
            'comp35',
            ]


        widgets = {
            'cab1num': forms.Select(attrs={'disabled': True}),
            'cab1': forms.Select(attrs={'disabled': True}),
            'cab1sides': forms.Select(attrs={'disabled': True}),
            'drwer1': forms.Select(attrs={'disabled': True}),
            'c11qty': forms.Select(attrs={'disabled': True}),
            'comp11': forms.Select(attrs={'disabled': True}),
            'c12qty': forms.Select(attrs={'disabled': True}),
            'comp12': forms.Select(attrs={'disabled': True}),
            'c13qty': forms.Select(attrs={'disabled': True}),
            'comp13': forms.Select(attrs={'disabled': True}),
            'c14qty': forms.Select(attrs={'disabled': True}),
            'comp14': forms.Select(attrs={'disabled': True}),
            'c15qty': forms.Select(attrs={'disabled': True}),
            'comp15': forms.Select(attrs={'disabled': True}),
            'cab2num': forms.Select(attrs={'disabled': True}),
            'cab2': forms.Select(attrs={'disabled': True}),
            'cab2sides': forms.Select(attrs={'disabled': True}),
            'drwer2': forms.Select(attrs={'disabled': True}),
            'c21qty': forms.Select(attrs={'disabled': True}),
            'comp21': forms.Select(attrs={'disabled': True}),
            'c22qty': forms.Select(attrs={'disabled': True}),
            'comp22': forms.Select(attrs={'disabled': True}),
            'c23qty': forms.Select(attrs={'disabled': True}),
            'comp23': forms.Select(attrs={'disabled': True}),
            'c24qty': forms.Select(attrs={'disabled': True}),
            'comp24': forms.Select(attrs={'disabled': True}),
            'c25qty': forms.Select(attrs={'disabled': True}),
            'comp25': forms.Select(attrs={'disabled': True}),
            'cab3num': forms.Select(attrs={'disabled': True}),
            'cab3': forms.Select(attrs={'disabled': True}),
            'cab3sides': forms.Select(attrs={'disabled': True}),
            'drwer3': forms.Select(attrs={'disabled': True}),
            'c31qty': forms.Select(attrs={'disabled': True}),
            'comp31': forms.Select(attrs={'disabled': True}),
            'c32qty': forms.Select(attrs={'disabled': True}),
            'comp32': forms.Select(attrs={'disabled': True}),
            'c33qty': forms.Select(attrs={'disabled': True}),
            'comp33': forms.Select(attrs={'disabled': True}),
            'c34qty': forms.Select(attrs={'disabled': True}),
            'comp34': forms.Select(attrs={'disabled': True}),
            'c35qty': forms.Select(attrs={'disabled': True}),
            'comp35': forms.Select(attrs={'disabled': True}),
            }


class RoomChoiceField(forms.Form):
    room = forms.ModelChoiceField(
        RoomType.objects.all(), to_field_name='id',
        required=False,
        empty_label='--------',
        label="")


class BidPage2(forms.ModelForm):
    class Meta:
        model = BidTbl2
        fields = [
            'cab4num',
            'cab4',
            'cab4sides',
            'drwer4',
            'c41qty',
            'comp41',
            'c42qty',
            'comp42',
            'c43qty',
            'comp43',
            'c44qty',
            'comp44',
            'c45qty',
            'comp45',
            'cab5num',
            'cab5',
            'cab5sides',
            'drwer5',
            'c51qty',
            'comp51',
            'c52qty',
            'comp52',
            'c53qty',
            'comp53',
            'c54qty',
            'comp54',
            'c55qty',
            'comp55',
            'cab6num',
            'cab6',
            'cab6sides',
            'drwer6',
            'c61qty',
            'comp61',
            'c62qty',
            'comp62',
            'c63qty',
            'comp63',
            'c64qty',
            'comp64',
            'c65qty',
            'comp65',

        ]

        widgets = {
            'cab4num': forms.Select(attrs={'disabled': True}),
            'cab4': forms.Select(attrs={'disabled': True}),
            'cab4sides': forms.Select(attrs={'disabled': True}),
            'drwer4': forms.Select(attrs={'disabled': True}),
            'c41qty': forms.Select(attrs={'disabled': True}),
            'comp41': forms.Select(attrs={'disabled': True}),
            'c42qty': forms.Select(attrs={'disabled': True}),
            'comp42': forms.Select(attrs={'disabled': True}),
            'c43qty': forms.Select(attrs={'disabled': True}),
            'comp43': forms.Select(attrs={'disabled': True}),
            'c44qty': forms.Select(attrs={'disabled': True}),
            'comp44': forms.Select(attrs={'disabled': True}),
            'c45qty': forms.Select(attrs={'disabled': True}),
            'comp45': forms.Select(attrs={'disabled': True}),
            'cab5num': forms.Select(attrs={'disabled': True}),
            'cab5': forms.Select(attrs={'disabled': True}),
            'cab5sides': forms.Select(attrs={'disabled': True}),
            'drwer5': forms.Select(attrs={'disabled': True}),
            'c51qty': forms.Select(attrs={'disabled': True}),
            'comp51': forms.Select(attrs={'disabled': True}),
            'c52qty': forms.Select(attrs={'disabled': True}),
            'comp52': forms.Select(attrs={'disabled': True}),
            'c53qty': forms.Select(attrs={'disabled': True}),
            'comp53': forms.Select(attrs={'disabled': True}),
            'c54qty': forms.Select(attrs={'disabled': True}),
            'comp54': forms.Select(attrs={'disabled': True}),
            'c55qty': forms.Select(attrs={'disabled': True}),
            'comp55': forms.Select(attrs={'disabled': True}),
            'cab6num': forms.Select(attrs={'disabled': True}),
            'cab6': forms.Select(attrs={'disabled': True}),
            'cab6sides': forms.Select(attrs={'disabled': True}),
            'drwer6': forms.Select(attrs={'disabled': True}),
            'c61qty': forms.Select(attrs={'disabled': True}),
            'comp61': forms.Select(attrs={'disabled': True}),
            'c62qty': forms.Select(attrs={'disabled': True}),
            'comp62': forms.Select(attrs={'disabled': True}),
            'c63qty': forms.Select(attrs={'disabled': True}),
            'comp63': forms.Select(attrs={'disabled': True}),
            'c64qty': forms.Select(attrs={'disabled': True}),
            'comp64': forms.Select(attrs={'disabled': True}),
            'c65qty': forms.Select(attrs={'disabled': True}),
            'comp65': forms.Select(attrs={'disabled': True}),
        }


class TotalRmCost(forms.ModelForm):
    class Meta:
        model = TotalRoomCost
        fields = [
            'bid_idA',
            'custid',
            'conid',
            'saleid',
            'custlastname',
            'custadd1',
            'room',
            'rmname',
            'cabnumtotal',
            'cabinet',
            'cabtotalprice',
            'cabsidenum',
            'cabsidecost',
            'cabsidetotal',
            'drawernum',
            'drawercost',
            'drawertotal',
            'optionnum',
            'custcabcost',
            'custcabtotal',
            'custsidecost',
            'custsidetotal',
            'cabaccrmtotal',
            'cabacccustom',
            'cabacctotal',
            'totalrmcost',
            'woodspecies',
            'woodspeciesperc',
            'wood',
            'door',
            'fncolor',
            'fnoption',
            'doorstyle',
            'doorstyleperc',
            'finishcolor',
            'finishcolorperc',
            'finishoption1',
            'finishoption1perc',
            'finishoption2',
            'finishoption2perc',
            'totalperc',
            'prodqueuetotal',
            'rmgrandtotal',

        ]



class AddNewRm(forms.ModelForm):

    class Meta:
        model = BidTbl
        fields = [
            'id',
            'bid_idA',
        ]


class JobCostForm(forms.ModelForm):

    class Meta:
        model = JobCost
        fields = [
            'jobid',
            'custid',
            'customtext',
            'discounttext',
            'constructiontext',
            'opt2text',
            'opt3text',
            'install',
            'customamount',
            'discountamount',
            'constructionamount',
            'opt2amount',
            'opt3amount',
            'installtext',
        ]


class CompLabor(forms.ModelForm):
    class Meta:
        model = CompOptionTotal
        fields = [
            'bid_idA',
            'custid',
            'conid',
            'jobid',
            'roomid',
            'compqty',
            'comp',
            'labor',
            'totallabor',

        ]


class CabinetLabor(forms.ModelForm):
    class Meta:
        model = Cabinet
        fields = [
            'bid_idA',
            'custid',
            'conid',
            'jobid',
            'roomid',
            'cabqty',
            'cablabor',
            'totalcablabor',

        ]


class DateInput2(forms.DateInput):
    input_type = 'date'


class ConTract(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            'id',
            'jobid',
            'custid',
            'workorderdate',
            'totalrmcost',
            'custom',
            'customtext',
            'construction',
            'constructiontext',
            'install',
            'discount',
            'discounttext',
            'opt1num',
            'opt1text',
            'opt2num',
            'opt2text',
            'opt3num',
            'opt3text',
            'taxrate',
            'tax',
            'subtotalcost',
            'totaljobcost',
            'grandtotalcost',
            'worktype',
            'memo1',
            'memo2',
            'memo3',
            'memo4',
            'memo5',
            'memo6',
            'memo7',
            'memo8',
            'memo9',
            'memo10',
            'memo11',
            'memo12',
            'memo13',
            'memo14',
            'memo15',
            'memo16',
            'memo17',
            'depositperc',
            'depositterms',
            'deposit',
            'depositdate',
            'pay2perc',
            'payment2',
            'terms2',
            'payment2date',
            'pay3perc',
            'terms3',
            'payment3',
            'payment3date',
            'pay4perc',
            'terms4',
            'payment4',
            'payment4date',
            'finalperc',
            'termsfinal',
            'finalpayment',
            'finalpaymentdate',
            'customdeposit',
            'seconddeposit',
            'thirddeposit',
            'forthdeposit',
            'agreementlist',
            'worktypelistdescr',
            'worktypedescr',
            'excludedescr',
            'includedescr',




        ]

    workorderdate = forms.DateField(
        widget=DateInput2(attrs={'onchange': 'WorkOrderDateFunction()'}),
        required=False,
    )

    depositdate = forms.DateField(
        widget=DateInput2(attrs={'onchange': 'DepositDateFunction()'}),
        required=False,
    )

    payment2date = forms.DateField(
        widget=DateInput2(attrs={'onchange': 'Deposit2DateFunction()'}),
        required=False,
    )

    payment3date = forms.DateField(
        widget=DateInput2(attrs={'onchange': 'Deposit3DateFunction()'}),
        required=False,
    )

    payment4date = forms.DateField(
        widget=DateInput2(attrs={'onchange': 'Deposit4DateFunction()'}),
        required=False,
    )

    finalpaymentdate = forms.DateField(
        widget=DateInput2(attrs={'onchange': 'FinalDateFunction()'}),
        required=False,
    )
