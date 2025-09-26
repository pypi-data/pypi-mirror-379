from typing import List

from pyPhasesRecordloader import AnnotationInvalid, AnnotationNotFound, Event
from pyPhasesRecordloader.recordLoaders.XMLAnnotationLoader import XMLAnnotationLoader


class NSRRAnnotationLoader(XMLAnnotationLoader):

    # MrOS groups: \|.*(?<!Periodic Breathing|Tachycardia|Blood pressure artifact|Arousal \(ARO SPONT\)|9|Arousal \(ARO RES\)|Mixed Apnea|Arousal \(ARO Limb\)|Arousal \(\)|RERA|Respiratory artifact|0|1|2|3|4|5|Central Apnea|Obstructive Apnea|Unsure|Hypopnea|Arousal \(ASDA\)|PLM \(Right\)|PLM \(Left\)|Limb Movement \(Left\)|SpO2 desaturation|SpO2 artifact|(Limb Movement \(Right\)))</EventConcept> ✅
    
    # SHHS groups: \|.*(?<!Arousal \(ARO RES\)|Periodic Breathing|Arousal \(External Arousal\)|Respiratory artifact|Mixed Apnea|9|6|Arousal \(ASDA\)|0|1|2|3|4|5|SpO2 desaturation|Arousal \(\)|Central Apnea|Obstructive Apnea|Unsure|Hypopnea|Arousal \(STANDARD\)|SpO2 artifact|Arousal \(CHESHIRE\))</EventConcept> ✅
    
    # MESA groups: \|.*(?<!Narrow Complex Tachycardia|RERA|Arousal \(ARO SPONT\)|Arousal \(ARO RES\)|Unsure|Arousal \(\)|Limb Movement \(Left\)|0|1|2|3|4|5|9|PLM \(Left\)|Periodic Breathing|Respiratory artifact|Mixed Apnea|Arousal \(ASDA\)|SpO2 desaturation|Central Apnea|Obstructive Apnea|Hypopnea|SpO2 artifact)</EventConcept>
    
    # (?<!Respiratory effort related arousal)\|RERA
    # (?<!ASDA arousal)\|Arousal.*</EventConcept>

    eventMaps = {
        "Stages|Stages": {
            "Wake|0": "W",
            "Stage 1 sleep|1": "N1",
            "Stage 2 sleep|2": "N2",
            "Stage 3 sleep|3": "N3",
            "Stage 4 sleep|4": "N3",
            "REM sleep|5": "R",
            # "Unsure|Unsure": "undefined",
            "Unscored|9": "undefined",
        },
        "Arousals|Arousals": {
            "Arousal|Arousal (STANDARD)": "arousal",
            "ASDA arousal|Arousal (ASDA)": "arousal_asda",
            "External arousal|Arousal (External Arousal)": "External arousal|Arousal (External Arousal)",
            "Arousal|Arousal ()": "arousal",
            "Arousal resulting from Chin EMG|Arousal (CHESHIRE)": "arousal_chin",
            "Arousal|Arousal (ARO Limb)": "arousal_limb",
            "Arousal resulting from respiratory effort|Arousal (ARO RES)": "arousal_respiratory",
            "Spontaneous arousal|Arousal (ARO SPONT)": "arousal_spontaneous",
        },
        "Respiratory|Respiratory": {
            "Mixed apnea|Mixed Apnea": "resp_mixedapnea",
            "Central apnea|Central Apnea": "resp_centralapnea",
            "Obstructive apnea|Obstructive Apnea": "resp_obstructiveapnea",
            "Hypopnea|Hypopnea": "resp_hypopnea",
            "Respiratory effort related arousal|RERA": "arousal_rera",
            "RERA|RERA": "arousal_rera", # is this used ?
        },
        "Limb Movement|Limb Movement": {
            "Periodic leg movement - right|PLM (Right)": "PLM-Right",
            "Periodic leg movement - left|PLM (Left)": "PLM-Left",
            "Limb movement - left|Limb Movement (Left)": "LegMovement-Left",
            "Limb movement - right|Limb Movement (Right)": "LegMovement-Right",
        }

    }

    # eventMapSpO2 = {
    #     "SpO2 desaturation|SpO2 desaturation": "spo2_desaturation",
    #     "SpO2 artifact|SpO2 artifact": "SpO2_artifact",
    # }

    # eventMapArtefacts = {
    #     "SpO2 artifact|SpO2 artifact": "SpO2_artifact",
    # }

    def getPath(self, xml, path):
        path = "./ScoredEvents/ScoredEvent" + path
        return xml.findall(path)

    def loadEvents(
        self,
        path,
        eventMap,
        durationChild="Duration",
        startChild="Start",
        typeChild="EventType",
        conceptChild="EventConcept",
        defaultState="ignore",
        minDuration=0,
        replaceName=None,
    ):
        tags = self.getPath(self.metaXML, path)
        if tags is None:
            raise AnnotationNotFound(path)

        events = []

        lastDefaultEvent = None
        for tag in tags:
            name = tag.find(conceptChild).text
            startValue = float(tag.find(startChild).text)
            if startValue is None:
                raise AnnotationInvalid(path + [startChild])

            startInSeconds = float(startValue)
            # if the name is in the eventMap it will be added to the annotations
            if name in eventMap:
                event = Event()
                event.start = startInSeconds
                event.manual = True
                eventName = replaceName(tag) if replaceName else eventMap[name]

                event.name = eventName

                if durationChild is not None:
                    # if there is a duration the event will be saved as as 2 events:
                    # startTime, "(eventName"
                    # endTime, "eventName)"
                    durationValue = float(tag.find(durationChild).text)
                    if durationValue is None:
                        raise AnnotationInvalid(path + [durationChild])

                    durationInSeconds = float(durationValue)
                    if durationInSeconds > minDuration:
                        event.duration = durationInSeconds
                        events.append(event)
                else:
                    # if its without a duration, it is considered a permanent state change
                    # that will persist until it is changed again
                    if lastDefaultEvent is not None:
                        lastDefaultEvent.duration = event.start - lastDefaultEvent.start
                    events.append(event)
                    lastDefaultEvent = event
            # else:
            #     self.logWarning("Event " + name + " not in EventMap.")

        if lastDefaultEvent is not None and self.lightOn is not None:
            lastDefaultEvent.duration = self.lightOn - lastDefaultEvent.start

        return events

    def loadAnnotation(self, xmlFile) -> List[Event]:
        self.loadXmlFile(xmlFile)

        allEvents = []

        for eventType, eventmap in self.eventMaps:
            allEvents += self.loadEvents(eventType, eventmap)

        self.lightOff = 0
        self.lightOn = None

        return allEvents

    def fillRecord(self, record, xmlFile):
        pass

