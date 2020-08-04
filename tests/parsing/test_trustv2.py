import unittest
from typing import List

from banyan.model.trustscore import TrustFactorsV2, TrustFactorDetailV2, TrustFactorV2
from banyan.model.user_device import TrustScore


class TrustScoreV2ParserTest(unittest.TestCase):
    def test_score(self):
        ts: List[TrustScore] = TrustScore.Schema().loads(open("tests/data/trust_scores.json").read(), many=True)
        self.assertEqual(2, len(ts))
        self.assertEqual('C02TQ08VHF1R', ts[0].trust_id)
        self.assertEqual(TrustScore.TRUST_TYPE_DEVICE, ts[0].trust_type)
        self.assertEqual('932f0800-556b-4296-a07c-92971a5c87c4', ts[0].factors.score_id)
        self.assertEqual('C02TQ08VHF1R', ts[1].trust_id)
        self.assertEqual(TrustScore.TRUST_TYPE_EXTERNAL, ts[1].trust_type)
        self.assertEqual('eb087ea4-25d1-4ee7-9f15-a9137411c170', ts[1].factors.score_id)


class TrustFactorV2ParserTest(unittest.TestCase):
    def test_factors(self):
        ts: TrustFactorsV2 = TrustFactorsV2.Schema().loads(open("tests/data/trust_factors.json").read())
        self.assertEqual('C02TQ08VHF1R', ts.resource_id)
        self.assertEqual(99, ts.score)
        self.assertEqual('device.algo', ts.score_type)

    def test_active_factor(self):
        ts: TrustFactorsV2 = TrustFactorsV2.Schema().loads(open("tests/data/trust_factors.json").read())
        f: List[TrustFactorV2] = [x for x in ts.active_factors if x.name == 'AutoUpdateEnabled']
        self.assertEqual(1, len(f))
        self.assertEqual('C02TQ08VHF1R', f[0].resource_id)
        self.assertIn('AutoUpdateEnabled', f[0].input_features.keys())
        self.assertEqual('true', f[0].value)
        self.assertEqual('true', f[0].input_features['AutoUpdateEnabled'])

    def test_inactive_factor(self):
        ts: TrustFactorsV2 = TrustFactorsV2.Schema().loads(open("tests/data/trust_factors.json").read())
        f: List[TrustFactorV2] = [x for x in ts.inactive_factors if x.name == 'NotJailbroken']
        self.assertEqual(1, len(f))
        self.assertEqual('C02TQ08VHF1R', f[0].resource_id)
        self.assertIn('NotJailbroken', f[0].input_features.keys())
        self.assertEqual('', f[0].value)
        self.assertEqual('', f[0].input_features['NotJailbroken'])

    def test_enabled_factor_detail(self):
        ts: TrustFactorsV2 = TrustFactorsV2.Schema().loads(open("tests/data/trust_factors.json").read())
        self.assertIn('AutoUpdateEnabled', ts.explanation.details.keys())
        d: TrustFactorDetailV2 = ts.explanation.details['AutoUpdateEnabled']
        self.assertEqual('AutoUpdateEnabled', d.factor_name)
        self.assertEqual('true', d.factor_value)
        self.assertEqual(True, d.is_active)
        self.assertEqual(1, d.relative_contribution)

    def test_disabled_factor_detail(self):
        ts: TrustFactorsV2 = TrustFactorsV2.Schema().loads(open("tests/data/trust_factors.json").read())
        self.assertIn('NotJailbroken', ts.explanation.details.keys())
        d = ts.explanation.details['NotJailbroken']
        self.assertEqual(False, d.is_active)
        self.assertEqual(0, d.relative_contribution)
