from pathlib import Path
from html.parser import HTMLParser
import re, unittest, hashlib
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__(); self.tags=[]; self.ids=[]; self.links=[]; self.feed(text)
 def handle_starttag(self,t,attrs):
  a=dict(attrs); self.tags.append((t,a))
  if 'id' in a:self.ids.append(a['id'])
  if t=='a': self.links.append(a.get('href',''))
class DraftChecks(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.html=Path('index.html').read_text();cls.page=Page(cls.html)
 def test_primary_need_give_actions(self):
  action=re.search(r'<div class="actions">(.*?)</div>',self.html,re.S).group(1)
  self.assertEqual(action.count('<a '),2)
  self.assertIn('I need food',action);self.assertIn('I have food to give',action)
  self.assertIn('Food banks &amp; registration',self.html)
 def test_reuse_checklist_secondary(self):
  block=self.html.split('id="your-city"')[1].split('</section>')[0]
  self.assertIn('<details>',block)
 def test_eight_fridge_cards(self): self.assertEqual(len(re.findall(r'<article class="location"(?: [^>]*)?>',self.html)),8)
 def test_compact_cards_keep_trip_essentials_visible(self):
  cards=re.findall(r'<article class="location"[^>]*>.*?</article>',self.html,re.S)
  self.assertEqual(len(cards),8)
  for card in cards:
   self.assertIn('<details class="card-more">',card)
   visible=card.split('<details class="card-more">')[0]
   for field in ['<h3>','class="address"','Vancouver, BC','Pickup','Hours','Entrance','class="map"']:
    self.assertIn(field,visible)
   self.assertRegex(visible,r'(rules apply|Check donation rules on site)')
   self.assertNotIn('<dt>Storage</dt>',visible)
   self.assertIn('<dt>Storage</dt>',card)
 def test_special_access_and_donation_limits_stay_visible(self):
  cards=re.findall(r'<article class="location"[^>]*>.*?</article>',self.html,re.S)
  victoria=next(c for c in cards if 'Victoria Drive community fridge' in c).split('<details class="card-more">')[0]
  self.assertIn('confirm labelling and handling before donating',victoria)
  main=next(c for c in cards if 'Main Street community fridge' in c).split('<details class="card-more">')[0]
  self.assertIn('Temporary location',main)
  self.assertIn('Exact fridge access is not described',main)
 def test_card_disclosures_have_names_and_sources(self):
  cards=re.findall(r'<article class="location"[^>]*>.*?</article>',self.html,re.S)
  for card in cards:
   more=card.split('<details class="card-more">')[-1]
   self.assertRegex(more,r'<summary aria-label="More details about [^"]+">More details</summary>')
   self.assertIn('Source checked 4 November 2026',more)
   self.assertIn('Give food',more)
 def test_neighbourhood_links_do_not_need_location(self):
  self.assertIn('aria-label="Jump to a neighbourhood"',self.html)
  for name in ['mount-pleasant','kitsilano','kensington-cedar-cottage','riley-park','kerrisdale','west-point-grey','grandview-woodland']:
   self.assertIn('href="#'+name+'"',self.html)
   self.assertIn(name,self.page.ids)
  self.assertNotIn('geolocation',self.html)
 def test_editor_still_linked_and_local(self):
  self.assertIn('href="starter.html"',self.html)
  editor=Path('starter.html').read_text()
  for id in ['make-kit','save-entry','project-file','site-preview']:self.assertIn('id="'+id+'"',editor)
  self.assertIn('src="starter.js"',editor)
 def test_new_project_contact_is_consistent(self):
  for file in ['index.html','preview.html','SECURITY.md']:
   text=Path(file).read_text()
   self.assertIn('Vancouverfoodshare.contact@gmail.com',text)
  for file in ['index.html','preview.html']:
   targets={href.split('?',1)[0] for href in Page(Path(file).read_text()).links if href.startswith('mailto:')}
   self.assertEqual(targets,{'mailto:Vancouverfoodshare.contact@gmail.com'})
  self.assertIn('Copyright (c) 2026 Adam Hind',Path('LICENSE.md').read_text())
 def test_resource_sections(self):
  for id in ['food-support','home-delivery','registration','host-interest','your-city']:self.assertIn(id,self.page.ids)
 def test_geography_and_delivery_are_separate(self):
  for copy in ['Outside Vancouver','Home delivery','Registration required','Paid · eligibility applies']:self.assertIn(copy,self.html)
 def test_host_interest_does_not_promise_operations(self):
  self.assertIn('no box, launch date or placement is promised',self.html)
  self.assertIn('mailto:Vancouverfoodshare.contact@gmail.com?subject=Food%20Share%20Hosting',self.html)
  self.assertIn('Nothing is submitted until you send the email',self.html)
 def test_reuse_prominent_and_local_obligations(self):
  self.assertIn('Bring Food Share to your city',self.html)
  self.assertIn('ADAPT_FOR_YOUR_CITY.md',self.html)
  for text in ['verify local locations','your own contact','your own QR code']:self.assertIn(text,self.html)
 def test_donation_warning(self):self.assertIn('does not accept household or pantry donations',self.html)
 def test_no_dynamic_collection(self):
  for tag,attrs in self.page.tags:self.assertNotIn(tag,['script','form','iframe','input'])
  self.assertIn("script-src 'none'",self.html);self.assertIn("form-action 'none'",self.html)
 def test_unique_and_valid_anchors(self):
  self.assertEqual(len(self.page.ids),len(set(self.page.ids)))
  for link in self.page.links:
   if link.startswith('#') and len(link)>1:self.assertIn(link[1:],self.page.ids)
 def test_only_safe_link_schemes(self):
  for link in self.page.links:self.assertTrue((link.startswith(('https://','mailto:','#')) or link=='starter.html'),link)
 def test_preview_parity(self):self.assertEqual(self.html,Path('preview.html').read_text())
 def test_preserve_uncertainties(self):
  for text in ['East Hastings LOAF','unconfirmed','Physical accessibility','No stock information','Temporary location']:self.assertIn(text,self.html)
 def test_source_dates_not_globally_refreshed(self):
  self.assertIn('2026-11-04',self.html);self.assertIn('Guidance source checked 16 October 2026',self.html)
 def test_publication_banner_removed(self):self.assertNotIn('Draft for review',self.html);self.assertNotIn('Live website unchanged',self.html)
if __name__=='__main__':unittest.main(verbosity=2)
