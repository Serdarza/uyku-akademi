#!/usr/bin/env python3
"""Download public research metadata. No automated clinical conclusions."""
import json, time, urllib.parse, urllib.request, datetime
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/"data"/"research.json"
def get(url):
    req=urllib.request.Request(url,headers={"User-Agent":"UykuAkademi/1.0 research-metadata"})
    with urllib.request.urlopen(req,timeout=35) as r:return json.load(r)
def pubmed():
    out={}
    base="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    terms=['("infant sleep"[Title/Abstract] OR "baby sleep"[Title/Abstract]) AND ("randomized controlled trial"[Publication Type] OR "systematic review"[Publication Type])','("pediatric sleep"[Title/Abstract] OR "child sleep"[Title/Abstract]) AND ("sleep intervention"[Title/Abstract] OR "sleep training"[Title/Abstract])','("safe sleep"[Title/Abstract] OR "sudden infant death syndrome"[Title/Abstract])']
    for term in terms:
        ids=get(base+"esearch.fcgi?"+urllib.parse.urlencode({"db":"pubmed","term":term,"retmode":"json","retmax":75,"sort":"date"}))["esearchresult"]["idlist"]
        time.sleep(.5)
        if not ids:continue
        summary=get(base+"esummary.fcgi?"+urllib.parse.urlencode({"db":"pubmed","id":",".join(ids),"retmode":"json"}))["result"]
        for pmid in ids:
            x=summary.get(pmid,{})
            if x.get("title"):out["PMID:"+pmid]={"source":"PubMed","id":"PMID:"+pmid,"title":x["title"],"date":x.get("pubdate",""),"url":"https://pubmed.ncbi.nlm.nih.gov/"+pmid+"/","review_status":"metadata_only"}
        time.sleep(.5)
    return list(out.values())
def trials():
    url="https://clinicaltrials.gov/api/v2/studies?"+urllib.parse.urlencode({"query.term":"infant sleep OR pediatric sleep","pageSize":100,"format":"json"})
    data=get(url)
    out=[]
    for x in data.get("studies",[]):
        p=x.get("protocolSection",{})
        ident=p.get("identificationModule",{})
        status=p.get("statusModule",{})
        nct=ident.get("nctId")
        if nct:out.append({"source":"ClinicalTrials.gov","id":nct,"title":ident.get("briefTitle",""),"date":status.get("studyFirstSubmitDate",""),"url":"https://clinicaltrials.gov/study/"+nct,"status":status.get("overallStatus",""),"review_status":"metadata_only"})
    return out
def main():
    records=[];errors=[]
    for label,func in [("PubMed",pubmed),("ClinicalTrials.gov",trials)]:
        try:records+=func()
        except Exception as exc:errors.append(label+": "+str(exc))
    if not records:raise SystemExit("No data received: "+"; ".join(errors))
    previous=[]
    if OUT.exists():
        try:previous=json.loads(OUT.read_text(encoding="utf-8")).get("records",[])
        except Exception:pass
    merged={x["id"]:x for x in previous if x.get("id")}
    merged.update({x["id"]:x for x in records if x.get("id")})
    payload={"updated_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),"records":list(merged.values())[:2000],"errors":errors,"methodology":"Bibliographic metadata only; expert review required"}
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("Saved",len(payload["records"]),"records",errors)
if __name__=="__main__":main()
