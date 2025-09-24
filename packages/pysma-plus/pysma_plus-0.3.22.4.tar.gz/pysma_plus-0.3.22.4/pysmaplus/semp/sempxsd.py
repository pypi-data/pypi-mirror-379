﻿# flake8: noqa
sempxsd: str = """<?xml version="1.0" encoding="utf-8"?>
<!--
# SEMP - Simple Energy Management Protocol
#
# Version: 1.3.0 , 2015-03-24
#
# SMA Solar Technology AG
# 34266 Niestetal, Germany
-->
<xs:schema targetNamespace="http://www.sma.de/communication/schema/SEMP/v1"
    elementFormDefault="qualified"
    xmlns="http://www.sma.de/communication/schema/SEMP/v1"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
>
  <xs:element name="Device2EM">
    <xs:annotation>
      <xs:documentation>
        This data structure encapsulates all information transmitted by the device to the Energy Management System
      </xs:documentation>
    </xs:annotation>
    <xs:complexType>
      <xs:sequence>
        <xs:element name="DeviceInfo" type="DeviceInfoType" minOccurs="0" maxOccurs="unbounded">
          <xs:annotation>
            <xs:documentation>
              A DeviceInfo encapsulates all static information about a device such as identification, capabilities, restrictions, etc.
            </xs:documentation>
          </xs:annotation>
        </xs:element>
        <xs:element name="DeviceStatus" type="DeviceStatusType"  minOccurs="0" maxOccurs="unbounded">
          <xs:annotation>
            <xs:documentation>
              A DeviceStatus encapsulates the status information of a device, i.e. all measurements and properties representing the current status of the device
            </xs:documentation>
          </xs:annotation>
        </xs:element>
        <xs:element name="PlanningRequest" type="PlanningRequestType" minOccurs="0" maxOccurs="unbounded">
          <xs:annotation>
            <xs:documentation>
              A PlanningRequest allows specification of the needs of the device with regard to energy, running time or a certain behaviour of sensor values.
              As long as an energy need is pending, the gateway has to announce them in terms of PlanningRequests.
              PlanningRequests are not incremental, i.e. requests that sent to the EM in previous messages are discarded
              and replaced by the newest PlanningRequests. Missing timeframes or an empty PlanningRequest list are interpreted
              as if the energy needs are already satisfied.
            </xs:documentation>
          </xs:annotation>
        </xs:element>
        <xs:element name="Messages" type="MessageListType" minOccurs="0" maxOccurs="1">
          <xs:annotation>
            <xs:documentation>
              This element provides information about an error or event the EM should be informed about.
            </xs:documentation>
          </xs:annotation>
        </xs:element>
        <xs:any namespace="##other" minOccurs="0" maxOccurs="unbounded" processContents="lax">
          <xs:annotation>
            <xs:documentation>
              Reserved for future use. Devices should ignore unknown elements.
            </xs:documentation>
          </xs:annotation>
        </xs:any>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
  
  <xs:element name="EM2Device">
    <xs:annotation>
      <xs:documentation>
        This data structure encapsulates all information transmitted by the Energy Management System to the device
      </xs:documentation>
    </xs:annotation>
    <xs:complexType>
      <xs:sequence>
        <xs:element name="DeviceControl" type="DeviceControlType" minOccurs="0" maxOccurs="unbounded">
          <xs:annotation>
            <xs:documentation>
              This element contains load control recommendations for a device.
            </xs:documentation>
          </xs:annotation>
        </xs:element>
        <xs:element name="Messages" type="MessageListType" minOccurs="0" maxOccurs="1">
          <xs:annotation>
            <xs:documentation>
              This element provides information about an error or event the device should be informed about.
            </xs:documentation>
          </xs:annotation>
        </xs:element>
        <xs:any namespace="##other" minOccurs="0" maxOccurs="unbounded" processContents="lax">
          <xs:annotation>
            <xs:documentation>
              Reserved for future use. Devices should ignore unknown elements.
            </xs:documentation>
          </xs:annotation>
        </xs:any>
      </xs:sequence>
    </xs:complexType>
  </xs:element>

  <xs:simpleType name="DeviceIdType">
    <xs:annotation>
      <xs:documentation>
        Type for unique device IDs.
        A device ID consists of a vendor ID type (VID type), a vendor ID (VID), a serial number and sub-device ID.
        <p/>
        The vendor ID should be globally unique. For this purpose either IANA PEN or IEEE OUI (known from MAC addresses) should be used. Although it is possible to define non-globally unique vendor IDs this option must not be used for products.
        The kind of vendor ID is defined by the vendor ID type. The following types are defined:
        <ul>
          <li>0x0: IANA PEN (32 bit, Format: 0xXXXXXXXX)</li>
          <li>0x1: IEEE OUI (24 bit, Format: 0x00XXXXXX)</li>
          <li>0xF: non-unique ID in local address space (32 bit). IMPORTANT: Use only for demos, examples or testing, not for products.</li>
        </ul>
        <p/>
        The serial number can be freely defined by the vendor as it specific to the vendor's address space. It must be unique for each of the vendor's devices.
        <p/>
        The sub-device ID can be used to point out, that a physical device consists of multiple virtual devices. The virtual device with sub-device ID 0 should be the main device. This information is only used to group devices in GUIs at the moment.
        <p/>
        Format: [VID Type:4bit]-[VID:32bit]-[Serial:48bit]-[SubDev-ID:8bit]
        Example 1: "0-00008CAD-112233445566-00" (IANA PEN: 36013)
        Example 2: "F-11223344-112233445566-00" (local address, only for testing, demos, examples)
      </xs:documentation>
    </xs:annotation>
    <xs:restriction base="xs:string">
      <xs:pattern value="[a-fA-F0-9]{1}-[a-fA-F0-9]{8}-[a-fA-F0-9]{12}-[a-fA-F0-9]{2}"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="RelOrAbsTimeType">
    <xs:annotation>
      <xs:documentation>
        Type representing timestamps that can either be relative (seconds relative to the current point of time) or absolute (Unix timestamp UTC in seconds since 01.01.1970).
        The device specifies the interpretation globally with the DeviceInfo.Capabilities.Timestamps element.
        Devices that do not have a synchronized clock (with time server protocols like NTP or radio control like DCF77) or do not have a reliable absolute time source should use relative timestamps.
      </xs:documentation>
    </xs:annotation>
    <xs:restriction base="xs:long"/>
  </xs:simpleType>
  
  <xs:complexType name="MessageListType">
    <xs:annotation>
      <xs:documentation>
        This type encapsulates a list of messages.
      </xs:documentation>
    </xs:annotation>
    <xs:sequence>
      <xs:element name="Message" type="MessageType" minOccurs="1" maxOccurs="unbounded">
        <xs:annotation>
          <xs:documentation>
            This element encapsulates information about an error or event.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
  <xs:simpleType name="MessageTypeRefType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="InvalidTimeframe"/>
      <xs:enumeration value="DeviceControlIgnored"/>
      <xs:enumeration value="Other"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="MessageLevelRefType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="Info"/>
      <xs:enumeration value="Warn"/>
      <xs:enumeration value="Error"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:complexType name="MessageType">
    <xs:annotation>
      <xs:documentation>
        This type encapsulates information about an error or event.
        It can also be used for data-tunnelling. In this case only the Type and Data elements might be set.
      </xs:documentation>
    </xs:annotation>
    <xs:sequence>
      <xs:element name="Type" type="xs:string" minOccurs="1" maxOccurs="1">
        <!-- ref=MessageTypeRefType -->
        <xs:annotation>
          <xs:documentation>
            The type of message used as a hint to interpret the message contents.
            See MessageTypeRefType for known values.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="Level" type="xs:string" minOccurs="0" maxOccurs="1">
        <!-- ref=MessageLevelRefType -->
        <xs:annotation>
          <xs:documentation>
            The severity of the message.
            See MessageLevelRefType for known values ("Info", "Warn", "Error").
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="Data" type="MessageDataType" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            Additional data describing the error or event (e.g. for automatic evaluation).
            For "InvalidTimeframe" the element DeviceId will be set.
            For "DeviceControlIgnored" the element DeviceId will be set.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="Text" type="xs:string" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            Description of the error/event.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="MessageDataType">
    <xs:annotation>
      <xs:documentation>
        Additional data describing the error/event.
      </xs:documentation>
    </xs:annotation>
    <xs:sequence>
      <xs:element name="DeviceId" type="DeviceIdType" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            Unique identification of the device this message applies to.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="Timestamp" type="RelOrAbsTimeType" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            Time of the occurrence of the error/event.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:any namespace="##other" minOccurs="0" maxOccurs="unbounded" processContents="lax">
        <xs:annotation>
          <xs:documentation>
            Reserved for future use. Devices should ignore unknown elements.
          </xs:documentation>
        </xs:annotation>
      </xs:any>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="DeviceInfoType">
    <xs:annotation>
      <xs:documentation>
        A DeviceInfo encapsulates all static information about a device such as identification, capabilities, restrictions, etc.
      </xs:documentation>
    </xs:annotation>
    <xs:sequence>
      <xs:element name="Identification" type="IdentificationType">
        <xs:annotation>
          <xs:documentation>
            General information for identifying the device.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="Characteristics" type="CharacteristicsType">
        <xs:annotation>
          <xs:documentation>
            Information on the characteristics of the device.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="Capabilities" type="CapabilitiesType">
        <xs:annotation>
          <xs:documentation>
            This element encapsulates information about the capabilities of the device
          </xs:documentation>
        </xs:annotation>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
  <xs:simpleType name="DeviceTypeRefType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="AirConditioning"/>
      <xs:enumeration value="Charger"/>
      <xs:enumeration value="DishWasher"/>
      <xs:enumeration value="Dryer"/>
      <xs:enumeration value="ElectricVehicle"/>
      <xs:enumeration value="EVCharger"/>
      <xs:enumeration value="Freezer"/>
      <xs:enumeration value="Fridge"/>
      <xs:enumeration value="Heater"/>
      <xs:enumeration value="HeatPump"/>
      <xs:enumeration value="Motor"/>
      <xs:enumeration value="Pump"/>
      <xs:enumeration value="WashingMachine"/>
      <xs:enumeration value="Other"/>
    </xs:restriction>
  </xs:simpleType> 
  <xs:complexType name="IdentificationType">
    <xs:annotation>
      <xs:documentation>
        General information for identifying the device.
      </xs:documentation>
    </xs:annotation>
    <xs:sequence>
      <xs:element name="DeviceId" type="DeviceIdType">
        <xs:annotation>
          <xs:documentation>
            Unique identification of the device.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="DeviceName" type="xs:string">
        <xs:annotation>
          <xs:documentation>
            Human readable device name
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="DeviceType" type="DeviceTypeRefType">
        <!-- ref=DeviceTypeRefType -->
        <xs:annotation>
          <xs:documentation>
            Human readable type of the device. See DeviceTypeRefType for well-known types.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="DeviceSerial" type="xs:string">
        <xs:annotation>
          <xs:documentation>
            Vendor specific serial number of the device
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="DeviceVendor" type="xs:string">
        <xs:annotation>
          <xs:documentation>
            Human readable name of the device vendor
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="DeviceURL" type="xs:string" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            Configuration URL of the device.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="CharacteristicsType">
    <xs:annotation>
      <xs:documentation>
        Information on the characteristics of the device.
      </xs:documentation>
    </xs:annotation>
    <xs:sequence>
      <xs:element name="MaxPowerConsumption" type="xs:int">
        <xs:annotation>
          <xs:documentation>
            Maximum power consumption of the device in Watts. If the device is controllable with regard to power consumption, the recommendation
            of the energy management system will never exceed this value.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="MinPowerConsumption" type="xs:int" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            If the device power is controllable by the EM, this element determines the minimum power consumption of the device. Recommendations
            of the energy management system will never go below this value.

            If the device power is not controllable by the EM, do not provide this element - only provide the MaxPowerConsumption. 
            This applies to fixed power devices as well as devices that use varying power-levels but are controllable in power by the EM
            (e.g. if the power varies between program phases but for each phase the power is fixed).
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="MinOnTime" type="xs:int" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            If the device is switched on, it has to remain in this status for at least MinOnTime seconds.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="MaxOnTime" type="xs:int" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            If the device is switched on, it must not remain on for more than MaxOnTime seconds.
            This element is for future use and not supported at the moment.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="MinOffTime" type="xs:int" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            If the device is switched off, it has to remain in this status for at least MinOffTime seconds.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="MaxOffTime" type="xs:int" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            If the device is switched off, it must not remain off for more than MaxOffTime seconds.
            This element is for future use and not supported at the moment.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="AddEnergySwitchOn" type="xs:double" minOccurs="0" maxOccurs="1" default="0">
        <xs:annotation>
          <xs:documentation>
            Amount of energy in Wh that is additionally needed if a device is switched on. This includes energy required for startup or warmup.
            This element is for future use and not supported at the moment.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="AddCostsSwitchOn" type="xs:double" minOccurs="0" maxOccurs="1" default="0">
        <xs:annotation>
          <xs:documentation>
            Price in Euros for the process of switching on the device. This excludes the cost for the operation. For example, this allows consideration of the limited lifetime of a corresponding relais or other kind of wear caused by switching.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="PowerLevels" type="PowerLevelsType" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            If the power consumption/generation can be controlled but only in a stepwise manner, the available steps are specified in the respective power levels in Watts.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="StandbyPower" type="xs:double" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            The maximum power consumed in standby mode. 
            This is used as threshold to detect inactivity of the device if a timeframe with KeepOnWhileConsumption enabled is used.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="StandbyTime" type="xs:int" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            The time that the power of a device has to remain below StandByPower until it is assumed to be in standby mode.
            This is used to detect inactivity of the device if a timeframe with KeepOnWhileConsumption enabled is used.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="CapabilitiesType">
    <xs:annotation>
      <xs:documentation>
        Encapsulates information about the capabilities of the device
      </xs:documentation>
    </xs:annotation>
    <xs:sequence>
      <xs:element name="CurrentPower" type="CapPowerMeasurementType">
        <xs:annotation>
          <xs:documentation>
            Capability of the device with regard to deriving information about its current power consumption, e.g. measurement or estimation
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="Sensor" type="SensorType" minOccurs="0" maxOccurs="10">
        <xs:annotation>
          <xs:documentation>
            Encapsulates information about a sensor attached to the device
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="Timestamps" type="CapTimestampType" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            Specifies if the device is able to deal with absolute timestamps or only with relative timestamps.
            Devices that do not have a synchronized clock (with time server protocols like NTP or radio control like DCF77) or do not have a reliable absolute time source should use relative timestamps.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="Interruptions" type="CapInterruptionsType" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            Specifies if a run of the device can be interrupted or not.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="Requests" type="CapRequestsType" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            Specifies options related to planning requests.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="PowerLevelsType">
    <xs:sequence>
      <xs:element name="PowerLevel" type="xs:double" minOccurs="1" maxOccurs="20">
        <xs:annotation>
          <xs:documentation>
            Power level in Watts [-100000, 100000] positive for consumption, negative for generation.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
  <xs:simpleType name="SensorTypeRefType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="Temperature"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="UnitOfMeasurementRefType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="DegreeCelsius"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:complexType name="SensorType">
    <xs:annotation>
      <xs:documentation>
        Encapsulates information about a sensor attached to the device
      </xs:documentation>
    </xs:annotation>
    <xs:sequence>
      <xs:element name="SensorId" type="xs:string">
        <xs:annotation>
          <xs:documentation>
            Unique identification of the sensor attached to the device. (64 bit identifier in the format XXXX-XXXXXXXX-XX-XX)
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="SensorType" type="xs:string">
        <!-- ref=SensorTypeRefType -->
        <xs:annotation>
          <xs:documentation>
            Type of the sensor. See SensorTypeRefType for known values (e.g. "Temperature").
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="SensorSemantic" type="xs:string" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            String providing information about the semantic of the sensor, e.g. temperature of the water supply
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="UnitOfMeasurement" type="xs:string" minOccurs="1" maxOccurs="1">
        <!-- ref=UnitOfMeasurementRefType -->
        <xs:annotation>
          <xs:documentation>
            String providing information about the unit of measurement.
            See UnitOfMeasurementRefType for known values (e.g. "DegreeCelsius").
          </xs:documentation>
        </xs:annotation>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
  <xs:simpleType name="PowerMeasurementMethodRefType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="Measurement"/>
      <xs:enumeration value="Estimation"/>
      <xs:enumeration value="None"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:complexType name="CapPowerMeasurementType">
    <xs:annotation>
      <xs:documentation>
        Capability of the device with regard to deriving information about its current power consumption, e.g. measurement or estimation
      </xs:documentation>
    </xs:annotation>
    <xs:sequence>
      <xs:element name="Method" type="xs:string">
        <!-- ref=PowerMeasurementMethodRefType -->
        <xs:annotation>
          <xs:documentation>
            String that defines the method of deriving information of the current power consumption.
            A device with a (built-in) power meter should use "Measurement". If it estimates the power consumption by look-up tables or other mechanisms select "Estimation".
            If it is not able to determine the power at all, "None" should be used.
            <p/>
            This information provides a hint about the quality of the power values provided in the device status section. It can be used to determine whether the power data can be used for learning device profile or to decide if it is suitable to be displayed.
            <p/>
            See PowerMeasurementMethodRefType for known values.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="CapTimestampType">
    <xs:annotation>
      <xs:documentation>
        Specifies if the device is able to deal with absolute timestamps or only with relative timestamps
      </xs:documentation>
    </xs:annotation>
    <xs:sequence>
      <xs:element name="AbsoluteTimestamps" type="xs:boolean" default="false">
        <xs:annotation>
          <xs:documentation>
            Bool that indicates if the device is able to deal with absolute timestamps or only with relative timestamps
          </xs:documentation>
        </xs:annotation>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="CapInterruptionsType">
    <xs:annotation>
      <xs:documentation>
        Specifies if a run of the device can be interrupted or not.
      </xs:documentation>
    </xs:annotation>
    <xs:sequence>
      <xs:element name="InterruptionsAllowed" type="xs:boolean" default="false">
        <xs:annotation>
          <xs:documentation>
            Bool that indicates if a run of the device can be interrupted (paused) or not.
            <p/>
            Allowing interruptions helps the EM to manage energy more flexibly. For instance the EM can interrupt a device in case of unpredictable bad weather conditions or when the user switches on a device with conflicting energy needs and restart it afterwards.
            <p/>
            Not all devices are able to handle interruptions during their runtime. In this case, the device will only be started by the EM and run until it is done.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="CapRequestsType">
    <xs:annotation>
      <xs:documentation>
        Specifies options related to planning requests.
      </xs:documentation>
    </xs:annotation>
    <xs:sequence>
      <xs:element name="OptionalEnergy" type="xs:boolean" default="false" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            This capability must be set to "true", if the device uses timeframes in planning requests with minRunningTime!=maxRunningTime or minEnergy!=maxEnergy. This is the case if the device is capable of consuming more (not essentially needed) energy if energy is cheap (e.g. by storing it). Otherwise it should be set to "false".
            <p/>
            As optional energy needs are defined by planning requests it is not possible for the EM to auto-detect this capability until the first optional demand was requested by the device.
            <p/>
            The information whether optional energy is requested is helpful as an EM might provide additional configuration options in a GUI when a device supports consuming optional energy. This might for example include constraints that define under which circumstances (price or ecological limits) optional energy is assigned to the device. Defining that a device is not capable of using optional energy helps the GUI to hide the complexity of defining these constraints from the user.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="StatusRefType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="On"/>
      <xs:enumeration value="Off"/>
      <xs:enumeration value="Offline"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:complexType name="DeviceStatusType">
    <xs:annotation>
      <xs:documentation>
        A DeviceStatus encapsulates the status information of a device, i.e. all measurements and properties representing the current status of the device
      </xs:documentation>
    </xs:annotation>
    <xs:sequence>
      <xs:element name="DeviceId" type="DeviceIdType">
        <xs:annotation>
          <xs:documentation>
            Unique identification of the device.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="EMSignalsAccepted" type="xs:boolean">
        <xs:annotation>
          <xs:documentation>
            Bool that indicates if the device is currently considering the control signals or recommendations provided by the energy manager or if it is
            in a mode which ignores the signals or recommendations
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="Status" type="xs:string">
        <!-- ref=StatusRefType -->
        <xs:annotation>
          <xs:documentation>
            String that provides information of the current status of the device (Offline, On, Off).
            See StatusRefType for known values.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="ErrorCode" type="xs:int" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            Identifies the current error state of the device. If the code is 0, no error is pending.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="PowerConsumption" type="PowerConsumptionType" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            Information about the current power consumption of the device, or the power consumption of the device since the last communication.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="SensorValues" type="SensorValuesType" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            Element encapsulating the measurements of the sensors associated with the device.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="PowerConsumptionType">
    <xs:annotation>
      <xs:documentation>
        Information about the current power consumption of the device, or the power consumption of the device since the last communication.
      </xs:documentation>
    </xs:annotation>
    <xs:sequence>
      <xs:element name="PowerInfo" type="PowerInfoType" minOccurs="1" maxOccurs="10">
        <xs:annotation>
          <xs:documentation>
            Information about a power consumption.
            </xs:documentation>
        </xs:annotation>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="PowerInfoType">
    <xs:annotation>
      <xs:documentation>
        Information about a power consumption.
      </xs:documentation>
    </xs:annotation>
    <xs:sequence>
      <xs:element name="AveragePower" type="xs:int">
        <xs:annotation>
          <xs:documentation>
            Real average power within the interval in Watts.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="MinPower" type="xs:int" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            Minimum power value within the interval in Watts.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="MaxPower" type="xs:int" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            Maximum power within the interval in Watts.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="Timestamp" type="RelOrAbsTimeType" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            Timestamp that represents the end of the averaging interval.
            Although this element is marked as optional it is mandatory in PowerConsumption:PowerInfo.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="AveragingInterval" type="xs:int" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            Length of the averaging interval in seconds.
            Although this element is marked as optional it is mandatory in PowerConsumption:PowerInfo.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="SensorValuesType">
    <xs:annotation>
      <xs:documentation>
        Provides a sequence of sensor readings
      </xs:documentation>
    </xs:annotation>    
    <xs:sequence>
      <xs:element name="SensorValue" type="SensorValueType" minOccurs="1" maxOccurs="10">
        <xs:annotation>
          <xs:documentation>
            Sequence of sensor measurements
          </xs:documentation>
        </xs:annotation>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="SensorValueType">
    <xs:annotation>
      <xs:documentation>
        Encapsulates the information about a sensor measurement in a certain time interval
      </xs:documentation>
    </xs:annotation>
    <xs:sequence>
      <xs:element name="SensorId" type="xs:string">
        <xs:annotation>
          <xs:documentation>
            Unique identification of the sensor attached to the device. (64 bit identifier in the format XXXX-XXXXXXXX-XX-XX)
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="AverageValue" type="xs:double">
        <xs:annotation>
          <xs:documentation>
            Average sensor value in the interval
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="Timestamp" type="RelOrAbsTimeType">
        <xs:annotation>
          <xs:documentation>
            Timestamp that represents the end of the interval.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="AveragingInterval" type="xs:int">
        <xs:annotation>
          <xs:documentation>
            Length of the averaging interval in seconds
          </xs:documentation>
        </xs:annotation>
      </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="PlanningRequestType">
    <xs:annotation>
      <xs:documentation>
        A PlanningRequest allows specification of the needs of the device with regard to energy, running time or a certain behaviour of sensor values within certain time frames.
      </xs:documentation>
    </xs:annotation>
    <xs:sequence>
      <xs:element name="Timeframe" type="TimeframeType" minOccurs="1" maxOccurs="unbounded">
        <xs:annotation>
          <xs:documentation>
            Sequence of timeframes that constitute the planning request.
            Timeframes for one device must not overlap (in terms of earliestStart and latestEnd) as a device can only
            run once at a time.
            In case timeframes overlap the EM has to modify them (e.g. merge or strip) which might lead to unexpected
            behavior.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
  <xs:simpleType name="PreferenceIndifferentAreasRefType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="NoPreference"/>
      <xs:enumeration value="Early"/>
      <xs:enumeration value="Late"/>
    </xs:restriction>
  </xs:simpleType>  
  <xs:complexType name="TimeframeType">
    <xs:annotation>
      <xs:documentation>
        Timeframe as part of a planning request, that allows specification of the energy needs of a device.
      </xs:documentation>
    </xs:annotation>
    <xs:sequence>
      <xs:element name="DeviceId" type="DeviceIdType">
        <xs:annotation>
          <xs:documentation>
            Unique identification of the device.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="EarliestStart" type="RelOrAbsTimeType">
        <xs:annotation>
          <xs:documentation>
            Represents the earliest possible time the device can be switched on by the EM.
            The combination of EarliestStart and LatestEnd specifies the interval in which the requested runtime or energy has to be allocated by the EM.
            
            If Min/MaxEnergy is used instead of Min/MaxRuntime, EarliestStart must not be in the past, i.e. contain a negative value, if relative timestamps are used.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="LatestEnd" type="RelOrAbsTimeType">
        <xs:annotation>
          <xs:documentation>
            Represents the latest possible end time the requested minimum runtime (MinRunningTime) or energy (MinEnergy) must be allocated to the device. This means at the given time the device operation must be finished. If a runtime was requested, the latest possible start of operation is LatestEnd-MinRunningTime. In case of an energy request, the latest start depends on the minimum amount of energy (MinEnergy) requested.

            The combination of EarliestStart and LatestEnd specifies the interval in which the requested runtime or energy has to be allocated by the EM.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="MinRunningTime" type="xs:int" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            Minimum running time within the timeframe in seconds.
            If MinRunningTime is 0, the operation of the device in this timeframe is optional.
            Defaults to 0 if MaxRunningTime is set.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="MaxRunningTime" type="xs:int" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            Maximum running time within the timeframe in seconds.
            If MinRunningTime equals MaxRunningTime, all of the given runtime is required. 
            If MinRunningTime is lower than MaxRunningTime, the amount of runtime given by MinRunningTime is required. The 
            runtime difference between MinRunningTime and MaxRunningTime is optional. That means that the EM will only assign the optional
            runtime to the device if certain conditions like ecological constraints and/or price of energy are met.
            Defaults to MinRunningTime if MinRunningTime is set.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="MinEnergy" type="xs:double" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            Minimum amount of electrical energy in Wh required within the timeframe.
            If MinEnergy is 0, the operation of the device in this timeframe is optional.
            Defaults to 0 if MaxEnergy is set.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="MaxEnergy" type="xs:double" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            Maximum amount of electrical energy in Wh that can be consumed or stored within the timeframe.
            If MinEnergy equals MaxEnergy, all of the given amount of energy is required. 
            If MinEnergy is lower than MaxEnergy, the amount of energy given by MinEnergy is required. The 
            energy difference between MinEnergy and MaxEnergy is optional. That means that the EM will only assign the optional
            energy to the device if certain conditions like ecological constraints and/or price of energy are met.
            Defaults to MinEnergy if MinEnergy is set.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="MaxPowerConsumption" type="xs:int" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            If the device is controllable with regard to power consumption, the recommendation of the energy management system will never exceed this value.
            This value overwrites the value provided by the MaxPowerConsumption element in the DeviceInfo. It must be less or equal than the value provided by the DeviceInfo.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="MinPowerConsumption" type="xs:int" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            If the device is controllable with regard to power consumption, the recommendation of the energy management system will never go below this value.
            This value overwrites the value provided by the MinPowerConsumption element in the DeviceInfo. It must be greater or equal than the value provided by the DeviceInfo.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="KeepOnWhileConsumption" type="xs:boolean" minOccurs="0" maxOccurs="1" default="false">
        <xs:annotation>
          <xs:documentation>
            Flag that indicates if the energy manager has to keep the control signal on, until no power consumption can be observed anymore.
            The DeviceInfo StandbyPower and StandbyTime parameters are used to detect inactivity. 
            Default values are used for these parameters if not specified by the device.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="PreferenceIndifferentAreas" type="xs:string" minOccurs="0" maxOccurs="1" default="NoPreference">
        <!-- ref=PreferenceIndifferentAreasRefType -->
        <xs:annotation>
          <xs:documentation>
            Indicates the preference within areas of indifferent price.
            That means if there are multiple possibilities to schedule a device with only small difference in prices
            the one according to the this preference is selected.
            If "Early" is selected, the earliest possibility is selected, for "Late" the latest. The default "NoPreference" 
            does not specify a preference, so the decision is made by the EM.
            See PreferenceIndifferentAreasRefType for known values.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="DeviceControlType">
    <xs:annotation>
      <xs:documentation>
        Contains operation and power consumption recommendations for a device.
      </xs:documentation>
    </xs:annotation>
    <xs:sequence>
      <xs:element name="DeviceId" type="DeviceIdType">
        <xs:annotation>
          <xs:documentation>
            Unique identification of the device.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="On" type="xs:boolean">
        <xs:annotation>
          <xs:documentation>
            Switch on/off recommendation.
            If On=true, the EM recommends that the device should be switched on or run its program.
            For interruptible devices On=false is a switch-off recommendation indicating that the device should switch off or pause.
            A device should follow the recommendation as soon as possible. Otherwise the device might interfere with other devices 
            managed by the EM.
            Note that the device should only accept a recommendation if stable operation is guaranteed (no risk of damage or safety issues).
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="RecommendedPowerConsumption" type="xs:double" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            Recommended power consumption in Watts
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="Timestamp" type="RelOrAbsTimeType">
        <xs:annotation>
          <xs:documentation>
            Timestamp of the generation of the message. 
            Note that this does not determine the activation time of the switch-on or power recommendation. Recommendations are supposed to be applied immediately by the device.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
</xs:schema>
"""
