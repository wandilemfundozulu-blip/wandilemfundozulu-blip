# 📊 Deloitte — Factory Telemetry & Equality Analysis

**Type:** Forage Data Analytics Job Simulation · **Completed:** 13 October 2026  
**Status:** Independent learning simulation; not employment with Deloitte.

## Business questions
- Which factories and device categories have the most unhealthy machine-status events?
- How should equality scores be grouped consistently across factories and job roles?

## Approach
I connected simulated Daikibo telemetry data in Tableau, developed an `Unhealthy` calculated field, and compared counts by factory and device type. In Excel, I worked with a table of factories, job roles and equality scores, using nested conditional logic to assign classifications.

## Findings
The Tableau screenshots indicated approximately **480 unhealthy events at Seiko**, **420 at Shenzhen**, **110 at Meiyo**, and **20 at Berlin**. These are approximate *event counts*, **not hours of downtime**.

An illustrative classification formula used in the exercise was:

```excel
=IF(OR(C2>20,C2<-20),"Highly Discriminative",IF(OR(C2>10,C2<-10),"Unfair","Fair"))
```

This version treats exact values of ±20 as **Unfair** and ±10 as **Fair**. Assessment screenshots also showed formula development, so this should not be taken as independent validation of the final workbook.

## Skills demonstrated
Tableau · JSON data interpretation · Calculated fields · Excel conditional formulas · Visual reporting

**Evidence scope:** This public summary is based on previously reviewed simulation screenshots and a workbook in a private working repository. It does not redistribute the simulation dataset or claim independently audited results.

[← Portfolio index](README.md)
