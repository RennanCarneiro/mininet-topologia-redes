# Static Routing Network Topology using Mininet

This project demonstrates the implementation of a custom network topology using **Mininet**, aimed at enabling inter-host communication through **static routing**. The exercise reinforces practical knowledge of IP addressing, subnetting, and routing configuration in simulated environments.

---

## Objective

To simulate a network environment with multiple subnets, interconnected via routers, and to enable end-to-end communication between hosts by manually configuring IP addresses and static routing tables.

---

## Topology Overview

The network consists of:

- **Routers**: `r1`, `r2`, `r3`  
- **Hosts**: `h1`, `h2`, `h3`, `h4`  
- **Point-to-point and LAN segments**:
  - `LAN1` (192.168.1.0/24): `h1`, `r1-eth0`
  - `LAN2` (192.168.2.0/24): `h2`, `r2-eth0`
  - `LAN3` (192.168.3.0/24): `h3`, `r3-eth1`
  - `LAN4` (192.168.4.0/24): `h4`, `r3-eth2`
  - `Link r1-r2` (10.0.0.0/30): `r1-eth1`, `r2-eth1`
  - `Link r2-r3` (10.0.1.0/30): `r2-eth2`, `r3-eth0`

### IP Addressing Scheme:

| Device       | Interface   | IP Address        | Subnet         |
|--------------|-------------|-------------------|----------------|
| h1           | -           | 192.168.1.10/24   | LAN1           |
| r1           | eth0        | 192.168.1.1/24    | LAN1           |
| r1           | eth1        | 10.0.0.1/30       | r1-r2 link     |
| r2           | eth0        | 192.168.2.1/24    | LAN2           |
| h2           | -           | 192.168.2.10/24   | LAN2           |
| r2           | eth1        | 10.0.0.2/30       | r1-r2 link     |
| r2           | eth2        | 10.0.1.1/30       | r2-r3 link     |
| r3           | eth0        | 10.0.1.2/30       | r2-r3 link     |
| r3           | eth1        | 192.168.3.1/24    | LAN3           |
| r3           | eth2        | 192.168.4.1/24    | LAN4           |
| h3           | -           | 192.168.3.10/24   | LAN3           |
| h4           | -           | 192.168.4.10/24   | LAN4           |

---

## Features & Technologies

- [x] Mininet (emulated network environment)
- [x] Static IP assignment
- [x] Manual routing table configuration
- [x] End-to-end connectivity verification

---

## How to Run

To execute this Mininet-based network topology and test the connectivity between the hosts, follow the steps below:

### 1. Prerequisites

Ensure that you have a working Mininet environment. This project was developed and tested in the **sdnhub VM**, commonly used for academic purposes. If you are using another environment, make sure Python and Mininet are correctly installed.

### 2. Clone the Repository

Clone the project to your local Mininet environment:

```bash
git clone https://github.com/RennanCarneiro/mininet-topologia-redes.git
cd mininet-topologia-redes

### 3. Run the custom topology

```bash
sudo python topologia.py

### 4. Access Hosts and Routers
To test configurations and connectivity, you can enter any host or router using the Mininet CLI

## Future Improvements

- Add automated tests for connectivity
- Include diagram generation from code
- Improve modularization of topology file

## Author

- **Rennan Carneiro** - [@RennanCarneiro](https://github.com/RennanCarneiro)