"""Tinian 16–24 June 1944: calibrated GHOST-day stage-1, sensitivity, not actual battle adjudication.
US casualties/ships/transport reset from prior-branch each day; Tinian gun physical/readiness/ammunition persist.
Historical confirmed US shore-gun interactions are maintained in a separate attribution ledger.
No air sortie forecast, no Saipan branch revision, no phase-2/3 feedback.
"""
from pathlib import Path
import json, csv, datetime
OUT=Path('/mnt/data')
# Core physical OOB (repo files 138, 150). Fractions are model expectations, never half a real gun.
# Rates, arc weights, target-contact scores are explicitly analytical controls, not identified shootings.
G=[
 dict(name='Ushi 140',category='140mm',phys=2.5,ready=1.5,nav_arc=1.00,ground_arc=.80,shot_rate=5.2),
 dict(name='Faibus 140',category='140mm',phys=2.5,ready=1.5,nav_arc=.70,ground_arc=.28,shot_rate=5.2),
 dict(name='Asiga 140',category='140mm',phys=4.0,ready=2.0,nav_arc=.55,ground_arc=.15,shot_rate=5.2),
 dict(name='Ushi 120 DP',category='120mm',phys=2.5,ready=1.8,nav_arc=.90,ground_arc=.75,shot_rate=7.0),
 dict(name='Other 120 DP',category='120mm',phys=5.5,ready=4.2,nav_arc=.25,ground_arc=.05,shot_rate=7.0),
 dict(name='Tinian Town 6in',category='6inch',phys=3.0,ready=2.0,nav_arc=.85,ground_arc=0.0,shot_rate=4.0),
 dict(name='Mobile 75',category='75mm',phys=10.0,ready=6.5,nav_arc=.18,ground_arc=.26,shot_rate=5.5),
]
# By caliber, post-June-15 hypothetical remaining accessible shells. Not a recovery of historic stocks!
STOCKS={'tight':{'140mm':110,'120mm':180,'6inch':55,'75mm':155},
        'center':{'140mm':330,'120mm':490,'6inch':155,'75mm':345},
        'deep':{'140mm':750,'120mm':1150,'6inch':330,'75mm':850}}
# The two system-comparisons start with exactly same 15-Jun-dawn physical OOB and each its own equal ammo.
SYS={'A-weak-recovery':dict(perm=.021,temp=.30,recover=.38),
     'B-fortified':dict(perm=.012,temp=.19,recover=.72)}
# Contact scores represent a sensitivity probe for qualifying targets, not proof of observed actual fire.
DAYS=[
 ('1944-06-16',.85,.75,.93,'After landing; NGFS continued; no named verified Tinian-to-US hull engagement'),
 ('1944-06-17',.82,.79,1.00,'Landing support and screening; no timed identified Tinian naval target'),
 ('1944-06-18',.78,.78,1.04,'Waller/Pringle east Saipan and Phelps west Saipan: NOT Tinian engagements'),
 ('1944-06-19',.78,.80,1.10,'Pringle attacked by Saipan east-shore fire; NOT Tinian'),
 ('1944-06-20',.72,.78,1.40,'US 531st Battery B starts Tinian 155-mm shelling; shore relief event remains conditional'),
 ('1944-06-21',.68,.73,1.45,'Existing US 155-mm counterbattery only; not all 531st batteries'),
 ('1944-06-22',.64,.66,1.53,'US ground guns/NGFS present; 531st B remains the known anti-Tinian Bty'),
 ('1944-06-23',.60,.64,1.60,'No sourced fixed Bty reenforcement before 24 Jun'),
 ('1944-06-24',.55,.58,2.14,'Other two 531st batteries turned to Tinian, tripled artillery component'),
]
# 'attack index' already integrates mixed ship / air / land pressure. 2.14 is scenario stress multiplier, NOT 3x all sources.
# These candidate ship minutes are *unconfirmed opportunities*: source-gated upper illustrations only.
BENCHMARK={'dday_tinian_B_total_batt_minutes':37,'dday_us_bb_ship_minutes':35,'dday_us_dd_ship_minutes':80,
           'rounds_per_firing_min_assumed':2.2,
           'within_day_contact_overlap_if_unconfirmed':.40,
           'within_day_replacement_fraction_assumed':.50}
# Sea-related 15 June benchmark includes gun/targets as whole Tinian system, not a single gun name.
REF_ASSUMED_B_NAVAL_ROUNDS=90.0
# Split of contact toward ship vs land is a target choice fraction, not two simultaneous salvos from same mount.
TARGET_NAV_SHARE=.72
rows=[];gunrows=[]
for stock_case,stk in STOCKS.items():
    for branch,sys in SYS.items():
        gunstate=[dict(x) for x in G]
        rounds_left=stk.copy()
        for day,contact_sea,contact_land,attack_scale,evidence in DAYS:
            candidates=[];totp=0;totr=0;sum_usable=0;fire_requests=[]
            # Initial intra-day suppression; virtual count resumption for partial day, then recovery at dusk.
            for x in gunstate:
                p=x['phys'];r=x['ready']; perm=min(p,p*sys['perm']*attack_scale)
                tmp=min(max(0,r-perm),r*sys['temp']*attack_scale)
                effective=max(0,r-perm-.5*tmp)
                # Japanese firing requests allocated either sea or ground targets, with distinct eligible arcs.
                request_naval=effective*x['nav_arc']*contact_sea*x['shot_rate']*TARGET_NAV_SHARE
                request_ground=effective*x['ground_arc']*contact_land*x['shot_rate']*(1-TARGET_NAV_SHARE)
                fire_requests.append([x,request_naval,request_ground,perm,tmp,effective,p,r])
            # Caliber-level shell cap allocates fractions proportional to requested shots across all guns of class,
            # never treats 140mm rounds as usable in 120mm or 6in mounts.
            bycat={}
            for x,nav,land,*rest in fire_requests:
                bycat[x['category']]=bycat.get(x['category'],0)+nav+land
            factors={cat:min(1.0,rounds_left[cat]/want) if want>0 else 1.0 for cat,want in bycat.items()}
            # use of fragments of a shot is a model expectation, not literal physical fractions
            d={'date':day,'stock_scenario':stock_case,'system':branch,'historical_gate':evidence,
               'US_ghost_start_restored':1,'aviation_unchanged':1,'Saipan_prior_branch_unchanged':1,
               'naval_contact_factor_UNVERIFIED':contact_sea,'land_contact_factor_UNVERIFIED':contact_land,
               'US_attack_pressure_assumed':attack_scale,'calibre_stock_initial_sum':sum(stk.values())}
            d['physical_before']=sum(x['phys'] for x in gunstate)
            d['ready_before']=sum(x['ready'] for x in gunstate)
            n_used=l_used=0
            for x,nav,land,perm,tmp,effective,p,r in fire_requests:
                k=factors[x['category']];n=nav*k;l=land*k
                n_used+=n;l_used+=l
                rounds_left[x['category']]-=n+l
                newphys=p-perm
                residual=max(0,p-r)+tmp
                rep= min(residual, sys['recover']*residual)
                newready=min(newphys,max(0,r-perm-tmp+rep))
                x['phys']=newphys;x['ready']=newready
                gunrows.append({'date':day,'stock_scenario':stock_case,'system':branch,'gun':x['name'],'caliber':x['category'],
                                'physical_before':p,'ready_before':r,'irreversible_loss':perm,'temporary_suppression':tmp,
                                'effective_ready_within_day':effective,'naval_arc_assumed':x['nav_arc'],'land_arc_assumed':x['ground_arc'],
                                'requested_naval_round_equiv':nav,'requested_land_round_equiv':land,'caliber_stock_throttle':k,
                                'fired_naval_round_equiv':n,'fired_land_round_equiv':l,'ready_next_morning':newready,'physical_next_morning':newphys,
                                'caliber_ammo_end':rounds_left[x['category']]})
            d['naval_eligible_round_equiv']=n_used
            d['land_eligible_round_equiv']=l_used
            d['total_fired_round_equiv']=n_used+l_used
            d['physical_next_dawn']=sum(x['phys'] for x in gunstate)
            d['ready_next_dawn']=sum(x['ready'] for x in gunstate)
            for cat in ('140mm','120mm','6inch','75mm'):d['stock_end_'+cat]=rounds_left[cat]
            d['all_stock_end']=sum(rounds_left.values())
            d['conditional_BBshipmin_UNVERIFIED']=35*n_used/REF_ASSUMED_B_NAVAL_ROUNDS
            d['conditional_DDshipmin_UNVERIFIED']=80*n_used/REF_ASSUMED_B_NAVAL_ROUNDS
            # Even upper latent opportunity is not a ship damage or actual fire interruption.
            d['US_ship_hits_confirmed_extra_Tinian']='NOT ESTABLISHED'
            d['US_personnel_loss_confirmed_extra_Tinian']='NOT ESTABLISHED'
            d['US_landing_delta_actual']='NOT ESTABLISHED'
            d['Japan_relief_delta_actual']='NOT ESTABLISHED'
            rows.append(d)
        for cat,rest in rounds_left.items():
            assert rest >= -1e-7, (stock_case,branch,cat,rest)
# compare paired daily
pairs=[]
for sc in STOCKS:
    for day,*_ in DAYS:
        a=next(x for x in rows if x['date']==day and x['system']=='A-weak-recovery' and x['stock_scenario']==sc)
        b=next(x for x in rows if x['date']==day and x['system']=='B-fortified' and x['stock_scenario']==sc)
        z={'date':day,'stock_scenario':sc,'US_ghost_reset_daily':1,'event_note':a['historical_gate'],
           'A_ready_next_dawn':a['ready_next_dawn'],'B_ready_next_dawn':b['ready_next_dawn'],
           'A_rounds_today':a['total_fired_round_equiv'],'B_rounds_today':b['total_fired_round_equiv'],
           'delta_rounds_today':b['total_fired_round_equiv']-a['total_fired_round_equiv'],
           'A_naval_round_equiv':a['naval_eligible_round_equiv'],'B_naval_round_equiv':b['naval_eligible_round_equiv'],
           'delta_naval_round_equiv':b['naval_eligible_round_equiv']-a['naval_eligible_round_equiv'],
           'A_ammo_remaining':a['all_stock_end'],'B_ammo_remaining':b['all_stock_end'],
           'A_BB_shipmin_latent':a['conditional_BBshipmin_UNVERIFIED'],
           'B_BB_shipmin_latent':b['conditional_BBshipmin_UNVERIFIED'],
           'A_DD_shipmin_latent':a['conditional_DDshipmin_UNVERIFIED'],
           'B_DD_shipmin_latent':b['conditional_DDshipmin_UNVERIFIED'],
           'delta_DD_shipmin_latent':b['conditional_DDshipmin_UNVERIFIED']-a['conditional_DDshipmin_UNVERIFIED'],
           'delta_DD_shipmin_same_day_AFTER_REPLACEMENT_IF_CONTACT':(b['conditional_DDshipmin_UNVERIFIED']-a['conditional_DDshipmin_UNVERIFIED'])*BENCHMARK['within_day_contact_overlap_if_unconfirmed']*(1-BENCHMARK['within_day_replacement_fraction_assumed']),
           'extra_US_hulls_sunk':'UNDETERMINED','extra_US_dead':'UNDETERMINED','extra_US_supply_not_received_t':'UNDETERMINED'}
        pairs.append(z)
# Evidence ledger: specific dates, named ships and location, no inappropriate Tinian booking
EVENTS=[
 {'date':'1944-06-14','time':'day','asset':'California BB-44 / Braine DD-630 / Cleveland CL-55','location':'Tinian fire support area','source':'Repo 150 and USN histories','observed':'California/Braine hit, Cleveland straddled (historical calibration)','attribution':'TINIAN HISTORICAL','delta_B_new':'NO: baseline historical event, must not count again'},
 {'date':'1944-06-15','time':'D-Day','asset':'Tennessee BB-43','location':'Southern Saipan support under Tinian fire','source':'Repo 133/151 and USN DANFS Tennessee','observed':'Three hits, 8 KIA and 25 WIA (historical); support continued','attribution':'TINIAN HISTORICAL','delta_B_new':'NO: historical already present; branch candidate extra localized effects pending'},
 {'date':'1944-06-16','time':'not established','asset':'US fire support vessels unspecified','location':'Southern Saipan/Tinian','source':'Repo 151, 153','observed':'Regular naval support; no named Tinian hit verified','attribution':'EXPOSURE CANDIDATE','delta_B_new':'NO ACTUAL HIT BOOKED'},
 {'date':'1944-06-17','time':'not established','asset':'US fire support vessels unspecified','location':'Southern Saipan/Tinian','source':'Repo 151, 153','observed':'Regular naval support; no named Tinian hit verified','attribution':'EXPOSURE CANDIDATE','delta_B_new':'NO ACTUAL HIT BOOKED'},
 {'date':'1944-06-18','time':'05:39','asset':'Phelps DD-360','location':'Saipan WEST shore south of Garapan','source':'USN damage report and Phelps action report','observed':'Two hits, one fireroom unfit; Saipan origin','attribution':'SAIPAN, NOT TINIAN','delta_B_new':'EXCLUDE'},
 {'date':'1944-06-18','time':'18:01','asset':'Waller DD-466, Pringle DD-477','location':'Magicienne Bay, Saipan EAST','source':'USN DANFS Waller','observed':'Saipan Japanese shore guns opened fire; maneuver/withdrawal','attribution':'SAIPAN, NOT TINIAN','delta_B_new':'EXCLUDE'},
 {'date':'1944-06-19','time':'early morning','asset':'Pringle DD-477','location':'Magicienne Bay, Saipan EAST','source':'USN DANFS Pringle','observed':'Came under shore fire; moved out of range, not hit','attribution':'SAIPAN, NOT TINIAN','delta_B_new':'EXCLUDE'},
 {'date':'1944-06-20','time':'evening','asset':'Pringle DD-477 -> Renshaw DD-499','location':'Magicienne Bay fire support station','source':'USN DANFS Pringle','observed':'Relieved on station; no Tinian encounter recorded in this entry','attribution':'US SUPPORT TRANSFER (not Tinian hit)','delta_B_new':'NO HIT BOOKED'},
 {'date':'1944-06-20','time':'day','asset':'Battery B, 531st FA / Tinian batteries','location':'Saipan artillery to Tinian','source':'USMC Seizure of Tinian','observed':'US 155-mm shelling of Tinian starts, continuing baseline pressure','attribution':'US FIRE ON TINIAN','delta_B_new':'APPLY TO TINIAN PHYSICAL/SUPPRESSION LOSS, no phantom US casualty'},
 {'date':'1944-06-21','time':'while under repair','asset':'Phelps DD-360','location':'Saipan','source':'USN wartime damage summary','observed':'Two small caliber hits from Japanese small craft during repairs; negligible damage','attribution':'SAIPAN SMALL CRAFT, NOT TINIAN','delta_B_new':'EXCLUDE'},
 {'date':'1944-06-22','time':'day/night','asset':'Pringle DD-477','location':'Special fire support mission, station unresolved','source':'USN DANFS Pringle','observed':'22–23 Jun special fire-support mission recorded; not a Tinian hit','attribution':'US SUPPORT CONTEXT','delta_B_new':'NO HIT BOOKED'},
 {'date':'1944-06-23','time':'day/night','asset':'Pringle DD-477','location':'Special fire support mission, station unresolved','source':'USN DANFS Pringle','observed':'22–23 Jun special fire-support mission recorded; not a Tinian hit','attribution':'US SUPPORT CONTEXT','delta_B_new':'NO HIT BOOKED'},
 {'date':'1944-06-24','time':'day','asset':'531st FA remaining Batteries A/C','location':'Saipan artillery to Tinian','source':'USMC Seizure of Tinian','observed':'Two additional 155-mm batteries turn to Tinian; total direct artillery component ~3x B-only','attribution':'US FIRE ON TINIAN','delta_B_new':'APPLY STRONGER BASELINE FIRE TO JAPAN; not all US fire tripled'},
]
for filename,rr in [('tinian_16_24_ghost_guns.csv',gunrows),('tinian_16_24_ghost_days.csv',rows),('tinian_16_24_ghost_deltas.csv',pairs),('tinian_16_24_evidence_events.csv',EVENTS)]:
    with (OUT/filename).open('w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f,fieldnames=list(rr[0].keys()));w.writeheader();w.writerows(rr)
SUM={}
for sc in STOCKS:
    q=[p for p in pairs if p['stock_scenario']==sc]
    SUM[sc]={'A_rounds_16_24':round(sum(x['A_rounds_today'] for x in q),1),
             'B_rounds_16_24':round(sum(x['B_rounds_today'] for x in q),1),
             'delta_rounds_16_24':round(sum(x['delta_rounds_today'] for x in q),1),
             'A_naval_16_24':round(sum(x['A_naval_round_equiv'] for x in q),1),
             'B_naval_16_24':round(sum(x['B_naval_round_equiv'] for x in q),1),
             'delta_naval_16_24':round(sum(x['delta_naval_round_equiv'] for x in q),1),
             'delta_latent_DD_shipmin':round(sum(x['delta_DD_shipmin_latent'] for x in q),1),
             'delta_unreplaced_DD_shipmin_if_contact':round(sum(x['delta_DD_shipmin_same_day_AFTER_REPLACEMENT_IF_CONTACT'] for x in q),1),
             'B_ammo_24_evening':{cat:round(next(z for z in rows if z['stock_scenario']==sc and z['system']=='B-fortified' and z['date']=='1944-06-24')['stock_end_'+cat],1) for cat in STOCKS[sc]},
             'actual_us_hit':'NOT DETERMINED'}
(OUT/'tinian_16_24_ghost_assumptions.json').write_text(json.dumps({'purpose':'Conditional potential accounting only, not historical adjudication','sources':['repo 133/134/138/150/151/153','USN DANFS Waller and Pringle','USN war damage Phelps','USMC 531st 20/24 Jun'], 'gun_groups':G,'stocks_post15_UNVERIFIED':STOCKS,'systems':SYS,'days':DAYS,'benchmark':BENCHMARK,'target_share_naval':TARGET_NAV_SHARE,'naval_benchmark_rounds_UNVERIFIED':REF_ASSUMED_B_NAVAL_ROUNDS,'summary':SUM},ensure_ascii=False,indent=2),encoding='utf-8')
print('SUMMARY')
for k,v in SUM.items():print(k,v)
print('\nCENTER DAILY')
for p in pairs:
    if p['stock_scenario']=='center':print(p['date'],*[round(p[k],2) for k in ('A_rounds_today','B_rounds_today','delta_rounds_today','A_ammo_remaining','B_ammo_remaining','delta_DD_shipmin_same_day_AFTER_REPLACEMENT_IF_CONTACT')])
assert len(gunrows)==9*7*2*3 and len(rows)==9*2*3 and len(pairs)==9*3
for case in STOCKS:
    for typ in SYS:
        subset=[v for v in rows if v['stock_scenario']==case and v['system']==typ]
        assert abs(sum(v['total_fired_round_equiv'] for v in subset)+subset[-1]['all_stock_end']-sum(STOCKS[case].values()))<1e-6