"""WORKING sensitivity: extends the existing 16–24 Jun ghost-day gun/ammo ledger through 6 July.
US baseline state resets each dawn; intra-day responses and suppression apply normally.
Japanese Tinian gun survival and ammo persist. No new aircraft, US named hull hits, Saipan extra guns,
Japanese convoy cargo, or post-branch US strategic reallocations are created.

The pre-Jun25 trace is checked numerically against the prior files before extending. All post-Jun24
contact and bombardment multipliers are explicit hypothetical inputs, not recovered fire logs.
"""
from __future__ import annotations
from pathlib import Path
import csv,json,zipfile,io,datetime,math
OUT=Path('/mnt/data')
with zipfile.ZipFile(OUT/'tinian_16_24_ghost_repro.zip') as arc:
    assum=json.loads(arc.read('tinian_16_24_ghost_assumptions.json'))

G=assum['gun_groups']; STOCKS=assum['stocks_post15_UNVERIFIED'];SYS=assum['systems']; BASE_DAYS=assum['days']; BMARK=assum['benchmark'];SHARE=assum['target_share_naval'];NAVREF=assum['naval_benchmark_rounds_UNVERIFIED']
# Source-anchored event existence, unverified contact/attack-strength model scalars.
# 26/27 also target the harbor/Tinian Town fortification cells independently of inter-island artillery.
EXTRA_DAYS=[
 ('1944-06-25',.64,.57,2.17,'Bancroft after arrival: night illumination/harassing Tinian Town/harbor; no Japanese hit established',1.22,1),
 ('1944-06-26',.82,.54,2.65,'Bancroft close shore; Birmingham+3 DD bombard town/harbor; five sampans historically lost, not carried to fork',1.65,1),
 ('1944-06-27',.74,.53,2.60,'Birmingham group bombardment after rearm; Town/harbor main suppression zone',1.62,1),
 ('1944-06-28',.57,.54,2.20,'Tinian bombardment continues; named cruiser contact not independently proven for date',1.00,0),
 ('1944-06-29',.57,.54,2.20,'155mm baseline; no dated new Tinian naval gun salvo established',1.00,0),
 ('1944-06-30',.55,.55,2.23,'155mm baseline; continuing shore support elsewhere',1.00,0),
 ('1944-07-01',.56,.56,2.20,'Birmingham historically at Garapan/Saipan, not a confirmed Tinian-target contact',1.00,0),
 ('1944-07-02',.53,.55,2.23,'US shore/naval fire continued; named contact unverified',1.00,0),
 ('1944-07-03',.52,.51,2.25,'155mm/shore+naval pressure illustrative',1.00,0),
 ('1944-07-04',.54,.54,2.28,'Aslito/Tinian threat; source-identified target and specific round counts unavailable',1.00,0),
 ('1944-07-05',.56,.56,2.30,'Birmingham at Saipan tank-support, do not duplicate as Tinian close mission',1.00,0),
 ('1944-07-06',.82,.55,2.75,'Birmingham fires at Tinian throughout day; Saipan final-operation remains prior-branch only',1.35,1),
]
# Protective shelter vs local direct fire in Town: sensitivity of extra physical/suppression losses only,
# not adding any US new attack beyond the source-anchored action class.
# A is not the prior branch in full: same gun state initially, weaker suppression recovery.
SCENARIOS={'soft':{'local_strike':.80,'contact':.60},'central':{'local_strike':1.00,'contact':1.00},'severe':{'local_strike':1.25,'contact':1.15}}
# Convert original 'Other 120 DP' on Jun25 to two fractions with exact preserved state.
# 4 of the 7 original other 120 guns were at Tinian Harbor/Town and 3 at Gurguan in file138.
def split_other120(guns):
    new=[]
    for x in guns:
        if x['name']!='Other 120 DP':new.append(x);continue
        for n,portion,sea,ground in [('Town 120 DP',4/7,.33,.0),('Gurguan 120 DP',3/7,.143333333333,.116666666667)]:
            z=dict(x);z['name']=n;z['phys']*=portion;z['ready']*=portion;z['nav_arc']=sea;z['ground_arc']=ground;new.append(z)
    return new

def step(guns,stock,s,day,contact_sea,contact_land,attack,event,local=1.,named=0,sensitivity='central'):
    details=[];req=[]
    for x in guns:
        p=x['phys'];r=x['ready']
        # Main guns close to Town attacked specifically on 25/26/27 and 6 Jul.
        local_target=x['name'] in ('Tinian Town 6in','Town 120 DP')
        local_factor=local if local_target else 1.0
        p_loss=min(p,p*s['perm']*attack*local_factor)
        suppressed=min(max(0,r-p_loss),r*s['temp']*attack*local_factor)
        eff=max(0,r-p_loss-.5*suppressed)
        naval=eff*x['nav_arc']*contact_sea*x['shot_rate']*SHARE
        land=eff*x['ground_arc']*contact_land*x['shot_rate']*(1-SHARE)
        req.append((x,p,r,p_loss,suppressed,eff,naval,land,local_target))
    tot_req={}
    for x,*rest in req:
        naval=rest[5];land=rest[6]
        tot_req[x['category']]=tot_req.get(x['category'],0.)+naval+land
    throttles={cat:min(1.,max(0,stock[cat])/want) if want>0 else 1. for cat,want in tot_req.items()}
    shotsea=shotland=shotntown=shotnamedntown=0.
    current = {'day':day,'event':event,'Aviation_preserved':1,'Saipan_prior_preserved':1,'US_daily_ghost_reset':1,
               'US_attack_pressure_assumed':attack,'named_Tinian_ship_mission_recorded':named,
               'sea_contact_assumed':contact_sea,'land_contact_assumed':contact_land,'town_attack_scalar':local,
               'physical_before':sum(g['phys'] for g in guns),'ready_before':sum(g['ready'] for g in guns)}
    for x,p,r,p_loss,suppressed,eff,naval,land,local_target in req:
        throttle=throttles[x['category']];nf=naval*throttle;lf=land*throttle
        shotsea+=nf;shotland+=lf
        if local_target:
            shotntown+=nf
            if named:shotnamedntown+=nf
        stock[x['category']]-=nf+lf
        newp=p-p_loss
        residual=max(0,p-r)+suppressed
        repaired=min(residual,s['recover']*residual)
        newr=min(newp,max(0,r-p_loss-suppressed+repaired))
        x['phys']=newp;x['ready']=newr
        details.append({'day':day,'sensitivity':sensitivity,'gun':x['name'],'caliber':x['category'],
           'physical_before':p,'ready_before':r,'irreversible_loss_expected':p_loss,'suppressed_expected':suppressed,
           'ready_in_day_expected':eff,'sea_shots_assumed':nf,'land_shots_assumed':lf,'ammo_throttle':throttle,
           'physical_next_morning':newp,'ready_next_morning':newr,'calibre_ammo_end':stock[x['category']],
           'named_ship_mission_day':named,'local_attack_intensity':local if local_target else 1.})
    current.update({'all_shots':shotsea+shotland,'sea_shots':shotsea,'land_shots':shotland,'town_6in_120_shots':shotntown,
                    'town_6in_120_shots_on_named_event_day':shotnamedntown,
                    'physical_next_morning':sum(g['phys'] for g in guns),'ready_next_morning':sum(g['ready'] for g in guns),
                    'ammo_all_end':sum(stock.values())})
    current.update({'ammo_end_'+k:stock[k] for k in ('140mm','120mm','6inch','75mm')})
    return current,details

with (OUT/'tinian_16_24_ghost_days.csv').open(encoding='utf-8-sig',newline='') as f:
    prior={(r['date'],r['stock_scenario'],r['system']):r for r in csv.DictReader(f)}

all_days=[];all_guns=[]
for stock_case,stock_initial in STOCKS.items():
 for branch,ss in SYS.items():
  for sensitivity,sens in SCENARIOS.items():
   guns=[dict(z) for z in G];stock=stock_initial.copy()
   for day,contact_sea,contact_land,attack,event in BASE_DAYS:
    d,ds=step(guns,stock,ss,day,contact_sea,contact_land,attack,event,1.,0,sensitivity)
    k=prior[(day,stock_case,branch)]
    assert abs(d['all_shots']-float(k['total_fired_round_equiv']))<1e-5, (day,d['all_shots'],k['total_fired_round_equiv'])
    assert abs(d['physical_next_morning']-float(k['physical_next_dawn']))<1e-5
   guns=split_other120(guns)
   for day,contact_sea,contact_land,attack,event,local,identified in EXTRA_DAYS:
    contact=contact_sea*sens['contact'];localfactor=1.+(local-1.)*sens['local_strike']
    d,ds=step(guns,stock,ss,day,contact,contact_land,attack,event,localfactor,identified,sensitivity)
    d.update({'stock_scenario':stock_case,'system':branch,'visibility_sensitivity':sensitivity,'sea_contact_scaled_assumed':contact,
              'town_ammo_increment_booked_from_new_shipments':0,'actual_US_ship_hit':'UNDETERMINED',
              'actual_US_casualties':'UNDETERMINED','actual_extra_JP_cargo_received_t':'UNDETERMINED',
              'actual_JP_port_ship_sunk':'UNDETERMINED'})
    for x in ds:x.update({'stock_scenario':stock_case,'system':branch})
    all_days.append(d);all_guns.extend(ds)
   assert all(v>=-1e-8 for v in stock.values())

paired=[]
for case in STOCKS:
 for sens in SCENARIOS:
  for day,*_ in EXTRA_DAYS:
   a=next(x for x in all_days if x['day']==day and x['stock_scenario']==case and x['visibility_sensitivity']==sens and x['system']=='A-weak-recovery')
   b=next(x for x in all_days if x['day']==day and x['stock_scenario']==case and x['visibility_sensitivity']==sens and x['system']=='B-fortified')
   pair={'day':day,'stock_scenario':case,'visibility_sensitivity':sens,'named_US_Tinian_mission':b['named_Tinian_ship_mission_recorded'],
         'A_ready_next':a['ready_next_morning'],'B_ready_next':b['ready_next_morning'],
         'A_physical_next':a['physical_next_morning'],'B_physical_next':b['physical_next_morning'],
         'A_shots':a['all_shots'],'B_shots':b['all_shots'],'delta_shots':b['all_shots']-a['all_shots'],
         'A_sea':a['sea_shots'],'B_sea':b['sea_shots'],'delta_sea':b['sea_shots']-a['sea_shots'],
         'A_land':a['land_shots'],'B_land':b['land_shots'],'delta_land':b['land_shots']-a['land_shots'],
         'A_town':a['town_6in_120_shots'],'B_town':b['town_6in_120_shots'],'delta_town':b['town_6in_120_shots']-a['town_6in_120_shots'],
         'B_140ammo_end':b['ammo_end_140mm'],'B_120ammo_end':b['ammo_end_120mm'],'B_6in_ammo_end':b['ammo_end_6inch'],'B_75ammo_end':b['ammo_end_75mm'],
         'extra_US_hulls_sunk':'UNDETERMINED','extra_US_dead':'UNDETERMINED','additional_JP_cargo_received_t':'UNDETERMINED'}
   paired.append(pair)

# For the *documented* close contact dates only: how much Town 6-inch gun fire in B could theoretically
# bear on a close DD/CL? Source evidence identifies the US target mission, not geometry/exposure of Japanese gun.
# 6-inch shells need a valid gun port traverse, visual target, firing decision, and ammunition.
for pair in paired:
    day=pair['day'];case=pair['stock_scenario'];sens=pair['visibility_sensitivity']
    town_guns=[x for x in all_guns if x['day']==day and x['stock_scenario']==case and x['system']=='B-fortified' and x['sensitivity']==sens and x['gun']=='Tinian Town 6in']
    pair['B_6inch_town_shots_target_opportunity']=town_guns[0]['sea_shots_assumed']
    # expose levels are *additional* assumptions, do not compute actual hit probability without reliable miss/hit calibration.
    pair['B_6inch_town_shots_at_25pct_exposure']=pair['B_6inch_town_shots_target_opportunity']*.25 if pair['named_US_Tinian_mission'] else 0
    pair['B_6inch_town_shots_at_50pct_exposure']=pair['B_6inch_town_shots_target_opportunity']*.5 if pair['named_US_Tinian_mission'] else 0
    pair['B_6inch_town_shots_at_75pct_exposure']=pair['B_6inch_town_shots_target_opportunity']*.75 if pair['named_US_Tinian_mission'] else 0

# A single real shell cannot appear in two roles; all sum checks explicitly.
assert len(all_days)==3*2*3*12 and len(all_guns)==len(all_days)*8
for case in STOCKS:
 for sys in SYS:
  for sens in SCENARIOS:
   rr=[x for x in all_days if x['stock_scenario']==case and x['system']==sys and x['visibility_sensitivity']==sens]
   original=prior[('1944-06-24',case,sys)]
   assert abs(sum(x['all_shots'] for x in rr)+rr[-1]['ammo_all_end']-float(original['all_stock_end']))<1e-5

def save_csv(filename,rows):
 with (OUT/filename).open('w',newline='',encoding='utf-8-sig') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0].keys()));w.writeheader();w.writerows(rows)
save_csv('tinian_25jul06_day_ghost.csv',all_days)
save_csv('tinian_25jul06_gunroll.csv',all_guns)
save_csv('tinian_25jul06_AB_deltas.csv',paired)

summaries=[]
for case in STOCKS:
 for sens in SCENARIOS:
  p=[x for x in paired if x['stock_scenario']==case and x['visibility_sensitivity']==sens]
  b=[x for x in all_days if x['stock_scenario']==case and x['visibility_sensitivity']==sens and x['system']=='B-fortified']
  aa=[x for x in all_days if x['stock_scenario']==case and x['visibility_sensitivity']==sens and x['system']=='A-weak-recovery']
  b6=[x for x in all_guns if x['stock_scenario']==case and x['sensitivity']==sens and x['system']=='B-fortified' and x['gun']=='Tinian Town 6in' and x['named_ship_mission_day']==1]
  summaries.append({'stock_scenario':case,'visibility_sensitivity':sens,'A_total_rounds':sum(x['all_shots'] for x in aa),
   'B_total_rounds':sum(x['all_shots'] for x in b),'delta_total_rounds':sum(x['delta_shots'] for x in p),
   'delta_sea_rounds':sum(x['delta_sea'] for x in p),'delta_land_rounds':sum(x['delta_land'] for x in p),
   'B_named_event_town_6inch_fire_opportunity':sum(x['sea_shots_assumed'] for x in b6),
   'B_named_event_town_6inch_shots_if_half_exposure':sum(x['sea_shots_assumed'] for x in b6)*.5,
   'B_ready_7Jul_am':b[-1]['ready_next_morning'],'B_physical_7Jul_am':b[-1]['physical_next_morning'],
   'B_ammo_rem_7Jul_am':b[-1]['ammo_all_end'],'B_6inch_stock_7Jul_am':b[-1]['ammo_end_6inch'],
   'B_140stock_7Jul_am':b[-1]['ammo_end_140mm'], 'B_120stock_7Jul_am':b[-1]['ammo_end_120mm']})
save_csv('tinian_25jul06_summary.csv',summaries)
(OUT/'tinian_25jul06_conditions.json').write_text(json.dumps({'description':'Diagnostic fixed-US daily ghost extension 25 Jun–6 July. Every rate / opportunity fractional weight is hypothetical and sensitive.','source':'tinian_16_24_ghost_assumptions.json and historical Navy records','note':'Gross B naval shots include prior Tinian fire; B-A is incremental vs controlled weak-recovery model, NOT fully reconstructed prior scenario.','post24_dates':EXTRA_DAYS,'scenario_sensitivity':SCENARIOS,'results':summaries},ensure_ascii=False,indent=2),encoding='utf-8')
print('SUMMARY 25 June–6 Jul')
for row in summaries:print(row['stock_scenario'],row['visibility_sensitivity'], 'A=',round(row['A_total_rounds'],1),'B=',round(row['B_total_rounds'],1),'delta=',round(row['delta_total_rounds'],1),'SEA DELTA=',round(row['delta_sea_rounds'],1),'TOWN 6inch named=',round(row['B_named_event_town_6inch_fire_opportunity'],1),'7jul B ready=',round(row['B_ready_7Jul_am'],1),'ammo=',round(row['B_ammo_rem_7Jul_am'],1))
print('CENTER CENTER DAY')
for x in paired:
 if x['stock_scenario']=='center' and x['visibility_sensitivity']=='central':print(x['day'],*[round(x[k],2) for k in ('B_shots','delta_shots','B_town','B_6inch_town_shots_target_opportunity','B_ready_next','B_140ammo_end','B_120ammo_end','B_6in_ammo_end')])