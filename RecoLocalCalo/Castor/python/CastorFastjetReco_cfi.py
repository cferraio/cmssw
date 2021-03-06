import FWCore.ParameterSet.Config as cms

from RecoJets.JetProducers.CaloJetParameters_cfi import *
from RecoJets.JetProducers.AnomalousCellParameters_cfi import *

CastorFastjetRecoAntiKt07 = cms.EDProducer(
    "FastjetJetProducer",
    CaloJetParameters,
    AnomalousCellParameters,
    jetAlgorithm = cms.string("AntiKt"),
    rParam       = cms.double(0.7)
    )
