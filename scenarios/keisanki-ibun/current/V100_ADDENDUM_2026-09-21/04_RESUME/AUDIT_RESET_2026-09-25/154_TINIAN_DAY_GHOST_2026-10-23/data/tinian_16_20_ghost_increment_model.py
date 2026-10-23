"""Tinian 16–20 Jun 1944: stage-1 day-only ghost extension, reproducible sensitivity.

Not a historical casualty/ship-damage finding. Gun physical/suppression/ammunition rolls across
successive days; additional US damage/reception effects do NOT carry to the next day's start.
Previous-branch Saipan artillery and the regional air audit are never reduced/recomputed.

A: counterfactual *weaker survivability* comparison starting from SAME 15 Jun dawn gun state.
B: fortified Tinian test. A is NOT an exact recovered prior-branch gun-by-gun ledger.
The model counts eligible fire opportunities and conditional US support attention, not actual hits.
"""
from __future__ import annotations
from pathlib import Path
import csv,json,datetime
O=Path('/mnt/data')
# Midpoints for 15 June B morning (repo 150); role masks are explicitly analytical,
# not measured historical traverse arcs: e.g. Asiga cannot shoot all west/north targets.
GUNS=[
 {"group":"Ushi 140", "p":2.5,"r":1.5,"target_weight":1.00,"category":"14cm"},
 {"group":"Faibus 140", "p":2.5,"r":1.5,"target_weight":0.65,"category":"14cm"},
 {"group":"Asiga 140", "p":4.0,"r":2.0,"target_weight":0.35,"category":"14cm"},
 {"group":"Ushi 120 DP", "p":2.5,"r":1.8,"target_weight":0.95,"category":"12cm"},
 {"group":"Other 120 DP", "p":5.5,"r":4.2,"target_weight":0.28,"category":"12cm"},
 {"group":"Tinian Town 6-inch", "p":3.0,"r":2.0,"target_weight":0.10,"category":"6inch"},
 {"group":"Mobile 75", "p":10.0,"r":6.5,"target_weight":0.20,"category":"75mm"},
]
INITIAL_WEIGHTED=sum(g['r']*g['target_weight'] for g in GUNS)
# Includes no residual 15-Jun shell inventories: these are explicit *post-15* examples.
CASES={
 'thin':{"stock":130.,"opportunity":.70,"US_intensity":1.35,"land_pressure":.75,"contact_overlap":.30,"replacement":.80},
 'middle':{"stock":320.,"opportunity":1.00,"US_intensity":1.00,"land_pressure":1.00,"contact_overlap":.50,"replacement":.50},
 'favorable':{"stock":850.,"opportunity":1.25,"US_intensity":.75,"land_pressure":1.15,"contact_overlap":.75,"replacement":.30},
}
# Dates source-gated; these are opportunity assumptions, NOT identified gun logs.
DAYS=[
 {"date":"1944-06-16","contact":.82,"BB_overlap":.62,"DD_overlap":.78,"US_attack_mult":.90,"evidence":"D-Day aftermath/NGFS continuing; no confirmed Tinian gun-hit this date"},
 {"date":"1944-06-17","contact":.74,"BB_overlap":.55,"DD_overlap":.76,"US_attack_mult":.98,"evidence":"Saipan support and coastal patrol; Tinian firing station not timed"},
 {"date":"1944-06-18","contact":.72,"BB_overlap":.50,"DD_overlap":.74,"US_attack_mult":1.05,"evidence":"Waller/Pringle were driven off by *Saipan* shore guns; cannot credit to Tinian"},
 {"date":"1944-06-19","contact":.69,"BB_overlap":.48,"DD_overlap":.71,"US_attack_mult":1.10,"evidence":"Pringle Saipan-east coast encounter, NOT Tinian; local gun records absent"},
 {"date":"1944-06-20","contact":.66,"BB_overlap":.50,"DD_overlap":.70,"US_attack_mult":1.38,"evidence":"US 531st Battery B 155mm first fires at Tinian; not all three batteries yet"},
]
# Gun opportunity time baseline and ship-minute calibrated from file151 for 15 Jun B.
BASE_DDAY_FIRE_MIN=37.0
BASE_BB_SHIP_MIN=35.0
BASE_DD_SHIP_MIN=80.0
# One effective group firing-minute -> expected fired rounds in this toy model.
ROUND_RATE=2.2
# fixed pressure is imposed without any NEW US deliberate countermeasure response; A/B differ
# only due to protection/recovery under identical attacks.
SURV={
 'A':{"irreversible":.021,"temporary":.30,"night_recovery":.38},
 'B':{"irreversible":.012,"temporary":.19,"night_recovery":.72},
}
ALL_ROWS=[];ALL_GROUPS=[];CARRY={};SUMMARY={}
for case,par in CASES.items():
   states={branch:[dict(g) for g in GUNS] for branch in ('A','B')}
   ammo={'A':par['stock'],'B':par['stock']}
   case_rows=[]
   for day in DAYS:
      datestr=day['date']; drow={'date':datestr,'condition':case,'evidence_gate':day['evidence'],
        'contact_factor_assumed':day['contact']*par['opportunity'],
        'bb_station_overlap_assumed':day['BB_overlap'],'dd_station_overlap_assumed':day['DD_overlap'],
        'US_pressure_assumed':day['US_attack_mult']*par['US_intensity'],
        'US_same_day_overlap':par['contact_overlap'],'US_same_day_replacement':par['replacement']}
      for branch in ('A','B'):
         weighted_day=0
         perm_all=0
         temp_all=0
         for g in states[branch]:
            prevP=g['p'];prevR=g['r']
            impact_scale=day['US_attack_mult']*par['US_intensity']
            perm=min(prevP,prevP*SURV[branch]['irreversible']*impact_scale)
            # suppression only among survivors previously active
            temp=min(max(0,prevR-perm),prevR*SURV[branch]['temporary']*impact_scale)
            # reaction fire before complete suppression: half the temporary silencing costs
            effective=max(0,prevR-perm-0.5*temp)
            weighted_day+=effective*g['target_weight']
            rest= max(0,prevP-prevR)+temp
            restore=min(rest,SURV[branch]['night_recovery']*rest)
            nextP=prevP-perm
            nextR=min(nextP,max(0,prevR-perm-temp+restore))
            g['p']=nextP;g['r']=nextR
            perm_all+=perm;temp_all+=temp
            ALL_GROUPS.append({'condition':case,'date':datestr,'branch':branch,'gun_group':g['group'],'physical_before':prevP,'ready_before':prevR,'permanent_loss_expected':perm,'temporary_suppressed_expected':temp,'effective_gun_equiv_during_day':effective,'physical_after':nextP,'ready_next_dawn':nextR,'range_arc_weight_assumed':g['target_weight']})
         # selection: opportunity ONLY when ships+land targets in firing geometry, not sustained max ROF.
         requested=BASE_DDAY_FIRE_MIN*(weighted_day/INITIAL_WEIGHTED)*day['contact']*par['opportunity']
         shot_req=requested*ROUND_RATE
         shot_used=min(ammo[branch],shot_req)
         fire=shot_used/ROUND_RATE
         ammo[branch]-=shot_used
         # At 15 Jun benchmark B ship overlap=1. Here both are constrained separately by target geometry.
         bb_m=BASE_BB_SHIP_MIN*fire/BASE_DDAY_FIRE_MIN*day['BB_overlap']
         dd_m=BASE_DD_SHIP_MIN*fire/BASE_DDAY_FIRE_MIN*day['DD_overlap']
         drow.update({f'{branch}_weighted_ready':weighted_day,f'{branch}_phys_lost_today':perm_all,
          f'{branch}_suppression_events_equiv':temp_all,f'{branch}_shots':shot_used,f'{branch}_fire_minutes':fire,
          f'{branch}_BB_attention_shipmin':bb_m,f'{branch}_DD_attention_shipmin':dd_m,
          f'{branch}_ammo_after':ammo[branch],f'{branch}_ready_next_dawn':sum(g['r']*g['target_weight'] for g in states[branch]),
          f'{branch}_physical_next_dawn':sum(g['p'] for g in states[branch])})
      for k in ('shots','fire_minutes','BB_attention_shipmin','DD_attention_shipmin','ready_next_dawn','physical_next_dawn'):
         drow['delta_'+k]=drow['B_'+k]-drow['A_'+k]
      # Appraisal: no demonstrated actual hit, casualties or unload interruption. All below are
      # possible intervals of ship attention if the Tinian fire overlaps corresponding stations.
      drow['delta_unreplaced_BB_shipmin_conditional']=drow['delta_BB_attention_shipmin']*par['contact_overlap']*(1-par['replacement'])
      drow['delta_unreplaced_DD_shipmin_conditional']=drow['delta_DD_attention_shipmin']*par['contact_overlap']*(1-par['replacement'])
      # The relief on 20/21 is a *separate old-branch candidate*, no automatic extra cargo.
      drow['Japanese_relief_reception_extra_t']='UNADJUDICATED'
      drow['American_landing_extra_queue_t']='UNADJUDICATED'
      drow['American_ship_hit_or_sunk']='UNADJUDICATED'
      drow['American_personnel_casualties']='UNADJUDICATED'
      drow['actual_uncovered_attention']='NOT VERIFIED: needs ship ID/target clock/contact overlap'
      ALL_ROWS.append(drow);case_rows.append(drow)
   SUMMARY[case]={
     'B_total_fire_min':sum(r['B_fire_minutes'] for r in case_rows),
     'A_total_fire_min':sum(r['A_fire_minutes'] for r in case_rows),
     'B_total_shots':sum(r['B_shots'] for r in case_rows),
     'A_total_shots':sum(r['A_shots'] for r in case_rows),
     'delta_BB_attention_shipmin':sum(r['delta_BB_attention_shipmin'] for r in case_rows),
     'delta_DD_attention_shipmin':sum(r['delta_DD_attention_shipmin'] for r in case_rows),
     'delta_unreplaced_BB_shipmin_conditional':sum(r['delta_unreplaced_BB_shipmin_conditional'] for r in case_rows),
     'delta_unreplaced_DD_shipmin_conditional':sum(r['delta_unreplaced_DD_shipmin_conditional'] for r in case_rows),
     'B_ammo_20_night':ammo['B'],'A_ammo_20_night':ammo['A'],
     'B_phys_after':case_rows[-1]['B_physical_next_dawn'],'A_phys_after':case_rows[-1]['A_physical_next_dawn'],
     'B_ready_after':case_rows[-1]['B_ready_next_dawn'],'A_ready_after':case_rows[-1]['A_ready_next_dawn'],
   }
# Double-bookkeeping checks
for s in CASES:
 x=[r for r in ALL_ROWS if r['condition']==s]
 assert len(x)==5
 assert all(r['B_shots']>=0 and r['A_shots']>=0 for r in x)
 assert sum(r['B_shots'] for r in x)<=CASES[s]['stock']+1e-8
 assert sum(r['A_shots'] for r in x)<=CASES[s]['stock']+1e-8
 assert all(r['B_physical_next_dawn']<=sum(g['p'] for g in GUNS)+1e-8 for r in x)
 assert all(r['American_ship_hit_or_sunk']=='UNADJUDICATED' for r in x)
 # Under a thin ammo wallet, better B survival can USE shells earlier, causing some later daily deltas to go negative.
 # This is a real accounting implication of the assumed finite common stocks, not an error.
 assert all(r['B_ammo_after']>=-1e-6 and r['A_ammo_after']>=-1e-6 for r in x)
for fn,data in [('tinian_16_20_daily.csv',ALL_ROWS),('tinian_16_20_gunroll.csv',ALL_GROUPS)]:
 with (O/fn).open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(data[0].keys()));w.writeheader();w.writerows(data)
(O/'tinian_16_20_parameters.json').write_text(json.dumps({'purpose':'Tinian 16-20 isolated same-day ghost conditional test, NOT measured hits','groups':GUNS,'scenarios':CASES,'events':DAYS,'survivability_coefficients_hypothetical':SURV,'file151_DDay_B_reference_ship_minutes':{'BB_CA':BASE_BB_SHIP_MIN,'DD':BASE_DD_SHIP_MIN,'fire_minutes':BASE_DDAY_FIRE_MIN},'rounds_per_effective_node_min_assumed':ROUND_RATE,'source_refs':['repo files 133,134,138,150,151,102','USN DANFS Waller & Pringle: 18-19 June Saipan not Tinian','USMC: 531st 155 mm first fire 20 June'],'summary':SUMMARY},ensure_ascii=False,indent=2),encoding='utf-8')
print('INITIAL weighted ready',INITIAL_WEIGHTED)
for s,ss in SUMMARY.items():print('SUMMARY',s,{k:round(v,2) for k,v in ss.items()})
for r in ALL_ROWS:
 if r['condition']=='middle':print(r['date'], 'B active min',round(r['B_fire_minutes'],2), 'A',round(r['A_fire_minutes'],2),'B ships BB/DD',round(r['B_BB_attention_shipmin'],2),round(r['B_DD_attention_shipmin'],2), 'delta BB/DD',round(r['delta_BB_attention_shipmin'],2),round(r['delta_DD_attention_shipmin'],2),'ammo',round(r['B_ammo_after'],1))