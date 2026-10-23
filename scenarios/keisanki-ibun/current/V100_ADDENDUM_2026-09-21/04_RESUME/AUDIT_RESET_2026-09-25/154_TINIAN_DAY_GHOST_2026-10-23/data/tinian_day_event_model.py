"""Tinian day-only ghost-rule: a transparent *counterfactual sensitivity calculator*.

All outputs labelled 'effect' are conditional, not historical measured casualties or new canonical outcomes.
For the 1944-06-15 local period, fixed anchors are sourced from GitHub file 151 and U.S. Navy
history on ~20,000 battle-ready marines ashore by sunset. 20/21 relief manifest from repo 104.
No aviation modeling; US casualties and hull availability reset at each subsequent morning.
"""
import csv, json, math
from pathlib import Path
O=Path('/mnt/data')
ANCHOR={
 'B_heavy_ship_minutes':35.,'B_dd_ship_minutes':80.,
 'B_heavy_range':[25.,45.],'B_dd_range':[60.,100.],
 'landed_by_sunset':20000.,'first_ashore_min':8*60+44,'illustrative_end_min':18*60+30,
 'relief_people_range':[490.,690.],'relief_cargo_range_t':[280.,440.],
 'relief_hypothetical_processing_minutes':240.,
}
# Approximate clock placements are demonstration positions, not the actual timestamps of shots.
EVENTS=[
 {'event':'T1','period':'08:20-08:32 (example)','start_min':8*60+20,'active_min':12.,'heavy_ship_min':12.,'dd_ship_min':24.,'post_first_landing':False,'description':'near H-hour ship/assault approach; do not count beach personnel flow before H'},
 {'event':'T2','period':'09:20-09:35 (example)','start_min':9*60+20,'active_min':15.,'heavy_ship_min':15.,'dd_ship_min':36.,'post_first_landing':True,'description':'postlanding support/boat congestion'},
 {'event':'T3','period':'11:05-11:15 (example)','start_min':11*60+5,'active_min':10.,'heavy_ship_min':8.,'dd_ship_min':20.,'post_first_landing':True,'description':'late morning reappearance'},
]
assert sum(e['active_min'] for e in EVENTS)==37
assert sum(e['heavy_ship_min'] for e in EVENTS)==ANCHOR['B_heavy_ship_minutes']
assert sum(e['dd_ship_min'] for e in EVENTS)==ANCHOR['B_dd_ship_minutes']

SCENARIOS={
 'low':{'overlap':0.25,'replacement':0.75,'beach_fraction':0.10,'beach_impairment':0.25,'T2T3_min':15.,'same_day_recovery':1.00,'dd_direct_hit_unfit_min':20.,'dd_doublecount_overlap':15.,'extra_window_min':0.},
 'center':{'overlap':0.50,'replacement':0.50,'beach_fraction':0.20,'beach_impairment':0.50,'T2T3_min':25.,'same_day_recovery':0.75,'dd_direct_hit_unfit_min':60.,'dd_doublecount_overlap':20.,'extra_window_min':10.},
 'high':{'overlap':0.80,'replacement':0.25,'beach_fraction':0.30,'beach_impairment':0.75,'T2T3_min':35.,'same_day_recovery':0.50,'dd_direct_hit_unfit_min':120.,'dd_doublecount_overlap':25.,'extra_window_min':20.},
}
flow=ANCHOR['landed_by_sunset']/(ANCHOR['illustrative_end_min']-ANCHOR['first_ashore_min'])
results=[]
for name, p in SCENARIOS.items():
 heavy_uncovered=35*p['overlap']*(1-p['replacement'])
 dd_uncovered=80*p['overlap']*(1-p['replacement'])
 queue=flow*p['T2T3_min']*p['beach_fraction']*p['beach_impairment']
 residual=queue*(1-p['same_day_recovery'])
 dd_added=max(0.,p['dd_direct_hit_unfit_min']-p['dd_doublecount_overlap'])
 minutes=p['extra_window_min']
 people_c=(490+690)/2/240*minutes
 cargo_c=(280+440)/2/240*minutes
 results.append({
 'scenario':name,**p,'full_front_benchmark_persons_per_min':flow,
 'unreplaced_heavy_ship_min':heavy_uncovered,'unreplaced_dd_ship_min':dd_uncovered,
 'gross_ship_min':115.,'dd_conditional_independent_damage_min':dd_added,
 'dd_total_burden_no_doublecount':80.+dd_added,
 'landing_flow_temporary_queue_person_equiv':queue,'landing_flow_recovered_same_day_person_equiv':queue*p['same_day_recovery'],
 'landing_flow_unrecovered_that_day_person_equiv':residual,
 'relief_candidate_extra_unloading_person_equiv':people_c,
 'relief_candidate_extra_unloading_t_equiv':cargo_c,
 'relief_actual_additional_personnel':'UNRESOLVED', 'relief_actual_additional_t':'UNRESOLVED',
 'ship_kills':'UNRESOLVED', 'marines_casualties':'UNRESOLVED',
 })
with (O/'tinian_day15_events.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(EVENTS[0]));w.writeheader();w.writerows(EVENTS)
with (O/'tinian_day15_scenarios.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(results[0]));w.writeheader();w.writerows(results)
(O/'tinian_day15_parameters.json').write_text(json.dumps({'anchors':ANCHOR,'events':EVENTS,'scenarios':SCENARIOS,'principles':{
 'baseline':'A old-branch detailed ship-minute not available => B gross only; B-A new numerical increment not claimed',
 'reset':'US morning state independently reset next day; Japanese physical gun/ammo stocks should carry forward in later ledger',
 'day15_shipminutes':'35 BB/CA + 80 DD/secondary: source 151, effects of counterbattery and cover',
 'counterbattery_vs_hit':'DD local direct-hit damage 20/60/120 min tested as extra ONLY after subtracting same-DD already-covered minutes',
 'reception':'persons/min benchmark uses approximate first landing 08:44 to illustrative end 18:30; not an observed beach-specific receiving rate',
 'relief':'20/21 branch S approved WORKING 490-690 personnel and 280-440t; 240 min rate is a hypothetical throughput test, NOT a discovered load/offload window',
 'air':'No air attrition or sortie computations; aerial suppression already enters base source 151 as a separate wallet',
 'US casualty and ship count':'Unknown, not zero; no fabricated named casualties or sinkings',
 }},ensure_ascii=False,indent=2),encoding='utf-8')
for q in results:
 print(q['scenario'], 'uncovered ship-min heavy/DD',round(q['unreplaced_heavy_ship_min'],2),round(q['unreplaced_dd_ship_min'],2), 'DD hit additional',q['dd_conditional_independent_damage_min'], 'landing queue temporary / residual',round(q['landing_flow_temporary_queue_person_equiv'],1),round(q['landing_flow_unrecovered_that_day_person_equiv'],1), '20/21  extra relief conversion t',round(q['relief_candidate_extra_unloading_t_equiv'],2))