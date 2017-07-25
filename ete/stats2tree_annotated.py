#!/usr/bin/python

import xml.dom.minidom as minidom
from ete3 import NCBITaxa, Tree, TreeStyle
import numpy as np
import pandas as pd

write_header=True
write_assembler_header=True

ncbi =NCBITaxa()
df=pd.read_csv("stats.csv", names=['taxid','CDS','CDS_Mean','exon','exon_Mean','gene','gene_Mean','mRNA','mRNA_Mean'])
taxid_list=df['taxid']

def get_leaves_taxid(nodeset):
    ncbi =NCBITaxa()
    df=pd.read_csv("stats.csv", names=['taxid','CDS','CDS_Mean','exon','exon_Mean','gene','gene_Mean','mRNA','mRNA_Mean'])
    taxid_list=df['taxid']
    gff_set=set()
    
    for nodeid in nodeset:
        for taxid in taxid_list:
            try:
                if nodeid in ncbi.get_lineage(taxid):
                    gff_set.add(taxid)
            except ValueError:
                print ("error in getting get_lineage()")

            
    return gff_set

def get_node_stats(tax_id): 
    
    info=df.loc[df['taxid'] == int(tax_id)].values.tolist()
    row=info[0]
    CDS=row[1]
    exon=row[3]
    gene=row[5]
    mRNA=row[7]
    tax2name= str(ncbi.translate_to_names([int(tax_id)]))[3:-2]
    return CDS,exon, gene, mRNA, tax2name

def get_node_describes(tax_id):
    taxid_list=get_leaves_taxid(set([int(tax_id)]))
    cds=df[df['taxid'].isin(taxid_list)]
    # another method to insert column to the datafram cds['parentTaxid']=tax_id
    cds.insert(0, "parentTaxid", tax_id)

    #write data fram to csv file
    # in an append mode
    global write_header
    if write_header==True:
        cds.to_csv('data1.csv', sep=',', mode='a', header=True)
        write_header=False
    else:
        cds.to_csv('data1.csv', sep=',', mode='a', header=False)
        
def get_node_assemblers(tax_id):
    taxid_list=get_leaves_taxid(set([int(tax_id)]))
    df=pd.read_csv("assemblers.csv", names=['taxid','assembler'])
    df=df[df['taxid'].isin(taxid_list)]
    df.insert(0, "parentTaxid", tax_id)
    #write data fram to csv file
    # in an append mode
    global write_assembler_header
    if write_assembler_header==True:
        df.to_csv('nodeAssembler.csv', sep=',', mode='a', header=True)
        write_assembler_header=False
    else:
        df.to_csv('nodeAssembler.csv', sep=',', mode='a', header=False)

        
def get_node_stats2(tax_id):
    taxid_list=get_leaves_taxid(set([int(tax_id)]))
    avg_CDS= df[df['taxid'].isin(taxid_list)]['CDS_Mean'].mean()
    avg_exon= df[df['taxid'].isin(taxid_list)]['exon_Mean'].mean()
    avg_gene= df[df['taxid'].isin(taxid_list)]['gene_Mean'].mean()
    avg_mRNA= df[df['taxid'].isin(taxid_list)]['mRNA_Mean'].mean()
    CDS_no= df[df['taxid'].isin(taxid_list)]['CDS'].mean()
    exon_no= df[df['taxid'].isin(taxid_list)]['exon'].mean()
    gene_no= df[df['taxid'].isin(taxid_list)]['gene'].mean()
    mRNA_no= df[df['taxid'].isin(taxid_list)]['mRNA'].mean()
    tax2name= str(ncbi.translate_to_names([int(tax_id)]))[3:-2]
    
    return avg_CDS,avg_exon, avg_gene, avg_mRNA,CDS_no,exon_no, gene_no, mRNA_no, tax2name


        
# get_node_assemblers(715989)
# get_node_describes(302)


 
def getTitles(xml):   
    doc = minidom.parse(xml)
    node = doc.documentElement
    clades = doc.getElementsByTagName("clade")
    
    taxonomy_list=[]
    for clade in clades:
        taxid=""
        taxonomy = clade.getElementsByTagName("taxonomy")[0]
        taxonomy_list.append(taxonomy)
        sci_name = taxonomy.getElementsByTagName("scientific_name")[0]
        nodes = sci_name.childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                taxid= node.data

        # <property ref="avg_CDS" datatype="xsd:string" applies_to="node">avg_CDS</property>        
        avg_CDS,avg_exon, avg_gene, avg_mRNA,CDS_no,exon_no, gene_no, mRNA_no, tax2name= get_node_stats2(taxid)
        
        # write all the nodes stats in a csv file
        get_node_describes(taxid)
        
        # write all the assemblers programs in a csv file
        get_node_assemblers(taxid)

        
 
        x = doc.createElement("name")  
        txt = doc.createTextNode(tax2name)  
        x.appendChild(txt)  
        clade.appendChild(x)  

        x = doc.createElement("property")  
        x.setAttribute("ref", "avg_CDS")
        x.setAttribute("datatype", "xsd:string")
        x.setAttribute("applies_to", "node")
        txt = doc.createTextNode(str(avg_CDS))  
        x.appendChild(txt)  
        clade.appendChild(x)  
        
        x = doc.createElement("property")  
        x.setAttribute("ref", "avg_exon")
        x.setAttribute("datatype", "xsd:string")
        x.setAttribute("applies_to", "node")
        txt = doc.createTextNode(str(avg_exon))  
        x.appendChild(txt)  
        clade.appendChild(x)
        
        x = doc.createElement("property")  
        x.setAttribute("ref", "avg_gene")
        x.setAttribute("datatype", "xsd:string")
        x.setAttribute("applies_to", "node")
        txt = doc.createTextNode(str(avg_gene))  
        x.appendChild(txt)  
        clade.appendChild(x) 
    
        x = doc.createElement("property")  
        x.setAttribute("ref", "avg_mRNA")
        x.setAttribute("datatype", "xsd:string")
        x.setAttribute("applies_to", "node")
        txt = doc.createTextNode(str(avg_mRNA))  
        x.appendChild(txt)  
        clade.appendChild(x)  
        
        x = doc.createElement("property")  
        x.setAttribute("ref", "mRNA_no")
        x.setAttribute("datatype", "xsd:string")
        x.setAttribute("applies_to", "node")
        txt = doc.createTextNode(str(mRNA_no))  
        x.appendChild(txt)  
        clade.appendChild(x)  
        
        x = doc.createElement("property")  
        x.setAttribute("ref", "gene_no")
        x.setAttribute("datatype", "xsd:string")
        x.setAttribute("applies_to", "node")
        txt = doc.createTextNode(str(gene_no))  
        x.appendChild(txt)  
        clade.appendChild(x)  
        
        x = doc.createElement("property")  
        x.setAttribute("ref", "exon_no")
        x.setAttribute("datatype", "xsd:string")
        x.setAttribute("applies_to", "node")
        txt = doc.createTextNode(str(exon_no))  
        x.appendChild(txt)  
        clade.appendChild(x)  
        
        x = doc.createElement("property")  
        x.setAttribute("ref", "CDS_no")
        x.setAttribute("datatype", "xsd:string")
        x.setAttribute("applies_to", "node")
        txt = doc.createTextNode(str(CDS_no))  
        x.appendChild(txt)  
        clade.appendChild(x)  
        
        
        #<property ref="See also1" applies_to="clade" datatype="xsd:anyURI"> url </property>
        ncbi_url="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=" + str(taxid)
        x = doc.createElement("property")  
        x.setAttribute("ref", "see ncbi:")
        x.setAttribute("datatype", "xsd:anyURI")
        x.setAttribute("applies_to", "node")
        txt = doc.createTextNode(ncbi_url)  
        x.appendChild(txt)  
        clade.appendChild(x)
        
        
    print(doc.toxml())
    with open ("NCBIPhylo_minidom.xml", 'w') as f:
        doc.writexml(f)

if __name__ == "__main__":
    document = 'NCBIPhylo.xml'
    getTitles(document)
    
    