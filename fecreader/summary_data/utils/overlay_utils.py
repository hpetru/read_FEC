from ftpdata.models import Candidate, Committee
from summary_data.models import Candidate_Overlay, District, Committee_Overlay
from summary_data.utils.term_reference import get_election_year_from_term_class, get_term_class_from_election_year
from summary_data.utils.party_reference import get_party_from_pty
from django.template.defaultfilters import slugify


def make_candidate_overlay_from_masterfile(candidate_id, cycle_to_copy_from=2014, election_year=2014, cycle_to_copy_to=2014, verify_does_not_exist=True):
    ## Returns overlay if created, None if not. 
    

    if verify_does_not_exist:
        try:
            # If there's already a candidate overlay, don't do this. 
            entered_candidate = Candidate_Overlay.objects.get(cycle=cycle_to_copy_to, fec_id=candidate_id)
            #print "Found candidate %s status %s" % (entered_candidate.name, entered_candidate.cand_ici)
            return None
        except Candidate_Overlay.DoesNotExist:
            pass

    thiscandidate = None
    
    try:
        thiscandidate = Candidate.objects.get(cycle=cycle_to_copy_from, cand_id=candidate_id, cand_election_year=election_year)
    except Candidate.DoesNotExist:
        print "Couldn't find candidate in masterfile id=%s election_year=%s cycle=%s" % (candidate_id, election_year, cycle_to_copy_from)
        return None
        
    
    state = thiscandidate.cand_office_st
    term_class = None
    if thiscandidate.cand_office == 'S':
        term_class = get_term_class_from_election_year(thiscandidate.cand_election_year)
    

    this_district = None
    try:
        if thiscandidate.cand_office == 'S':
            this_district = District.objects.get(election_year=election_year, state=state, office=thiscandidate.cand_office, term_class=term_class)
        elif thiscandidate.cand_office == 'H':
            this_district = District.objects.get(election_year=election_year, state=state, office=thiscandidate.cand_office, office_district=thiscandidate.cand_office_district)
        elif thiscandidate.cand_office == 'P':
            # there's no district, so pass
            # do we need a presidential placeholder ? 
            pass
    except District.DoesNotExist:
        print "!! Invalid district for %s %s %s %s" % (thiscandidate.cand_name, term_class, thiscandidate.cand_election_year, state)
        return None
    
    co = Candidate_Overlay.objects.create(
            district=this_district,
            office_district=thiscandidate.cand_office_district,
            cycle=cycle_to_copy_to,
            fec_id=candidate_id,
            name=thiscandidate.cand_name,
            slug = slugify(thiscandidate.cand_name),
            pty=thiscandidate.cand_pty_affiliation,
            party = get_party_from_pty(thiscandidate.cand_pty_affiliation),
            pcc=thiscandidate.cand_pcc,
            term_class=term_class,
            election_year=thiscandidate.cand_election_year,
            curated_election_year=thiscandidate.cand_election_year,
            state=thiscandidate.cand_office_st,
            office=thiscandidate.cand_office,
            cand_ici=thiscandidate.cand_ici,
            candidate_status='D'
    )
    return co
    
    
def make_committee_overlay_from_masterfile(committee_id, cycle_to_copy_from=2014, cycle_to_copy_to=2014, verify_does_not_exist=True):
    c = Committee.objects.get(cmte_id=committee_id, cycle=cycle_to_copy_from)
    
    if verify_does_not_exist:
        try:
            Committee_Overlay.objects.get(fec_id=committee_id, cycle=cycle_to_copy_from)
            return None
        except Committee_Overlay.DoesNotExist:
            pass
    ctype = c.cmte_tp
    is_hybrid = False
    is_noncommittee = False
    is_superpac = False
    if ctype:
        if ctype.upper() in ['O', 'U']:
            is_superpac = True
        if ctype.upper() in ['V', 'W']:
            is_hybrid = True
        if ctype.upper() in ['I']:
            is_noncommittee = True
        
    party = c.cmte_pty_affiliation
    if party:
        party = get_party_from_pty(party)
    
    cm = Committee_Overlay.objects.create(
        cycle = cycle_to_copy_to,
        name = c.cmte_name,
        fec_id = c.cmte_id,
        slug = slugify(c.cmte_name),
        party = party,
        treasurer = c.tres_nm,
        street_1 = c.cmte_st1,
        street_2 = c.cmte_st2,
        city = c.cmte_city,
        state = c.cmte_st,
        connected_org_name = c.connected_org_nm,
        filing_frequency = c.cmte_filing_freq,
        candidate_id = c.cand_id,
        is_superpac = is_superpac,
        is_hybrid = is_hybrid,
        is_noncommittee = is_noncommittee,
        designation = c.cmte_dsgn,
        ctype = ctype,
    )
    
    return cm
    
    

"""
from summary_data.utils.overlay_utils import make_candidate_overlay_from_masterfile
make_candidate_overlay_from_masterfile('H0CA48024') # issa
make_candidate_overlay_from_masterfile('S8NC00239') # hagan

from summary_data.utils.overlay_utils import make_committee_overlay_from_masterfile
make_committee_overlay_from_masterfile('C00542779')


"""