import os,sys
import subprocess
import MySQLdb
from PyQt4 import QtCore


class DatabaseCreator(object):
	def __init__(self,newDatabaseName,parent=None):
		self.si_om=parent
		self.newDatabaseName = newDatabaseName
		self.sqldump = """-- phpMyAdmin SQL Dump
		-- version 4.0.4
		-- http://www.phpmyadmin.net
		--
		-- Host: localhost
		-- Generation Time: Feb 06, 2015 at 10:47 PM
		-- Server version: 5.6.12-log
		-- PHP Version: 5.4.12

		SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
		SET time_zone = "+00:00";


		/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
		/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
		/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
		/*!40101 SET NAMES utf8 */;

		--
		-- Database: `"""+newDatabaseName+"""`
		--
		CREATE DATABASE IF NOT EXISTS `"""+newDatabaseName+"""` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
		USE `"""+newDatabaseName+"""`;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_bank`
		--

		CREATE TABLE IF NOT EXISTS `gd_bank` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeRekening` varchar(64) NOT NULL,
		  `nomorRekening` varchar(100) NOT NULL,
		  `anRekening` varchar(128) NOT NULL,
		  `cabangBank` varchar(128) NOT NULL,
		  `alamatBank` varchar(256) NOT NULL,
		  `kontakBank` varchar(64) NOT NULL,
		  PRIMARY KEY (`id`),
		  UNIQUE KEY `kodeRekening` (`kodeRekening`,`nomorRekening`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_bank_keluar`
		--

		CREATE TABLE IF NOT EXISTS `gd_bank_keluar` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `tanggal` date NOT NULL,
		  `catatan` varchar(512) NOT NULL,
		  `nilaiTotal` double NOT NULL,
		  `noAkunBank` varchar(10) NOT NULL,
		  `kodePelanggan` varchar(64) NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_bank_masuk`
		--

		CREATE TABLE IF NOT EXISTS `gd_bank_masuk` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `tanggal` date NOT NULL,
		  `catatan` varchar(512) NOT NULL,
		  `nilaiTotal` double NOT NULL,
		  `noAkunBank` varchar(10) NOT NULL,
		  `kodePelanggan` varchar(64) NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_bayar`
		--

		CREATE TABLE IF NOT EXISTS `gd_bayar` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodePelanggan` varchar(64) NOT NULL,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `kodeRekening` varchar(64) NOT NULL,
		  `jumlahDibayar` double NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_buku_besar`
		--

		CREATE TABLE IF NOT EXISTS `gd_buku_besar` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `tanggal` date NOT NULL,
		  `noAkun` varchar(10) NOT NULL,
		  `debit` double NOT NULL,
		  `kredit` double NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_data_departemen`
		--

		CREATE TABLE IF NOT EXISTS `gd_data_departemen` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeDepartemen` varchar(64) NOT NULL,
		  `namaDepartemen` varchar(256) NOT NULL,
		  `parentDepartemen` varchar(64) NOT NULL,
		  `kodePenjab` varchar(64) NOT NULL,
		  `catatan` varchar(384) NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_data_gudang`
		--

		CREATE TABLE IF NOT EXISTS `gd_data_gudang` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeGudang` varchar(64) NOT NULL,
		  `namaGudang` varchar(64) NOT NULL,
		  `lokasi` varchar(256) NOT NULL,
		  PRIMARY KEY (`id`),
		  UNIQUE KEY `kodeGudang` (`kodeGudang`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_data_pajak`
		--

		CREATE TABLE IF NOT EXISTS `gd_data_pajak` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodePajak` varchar(64) NOT NULL,
		  `namaPajak` varchar(100) NOT NULL,
		  `persenPajak` double NOT NULL,
		  `keterangan` varchar(256) NOT NULL,
		  PRIMARY KEY (`id`),
		  UNIQUE KEY `kodePajak` (`kodePajak`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_data_penyimpanan`
		--

		CREATE TABLE IF NOT EXISTS `gd_data_penyimpanan` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeBarang` varchar(64) NOT NULL,
		  `tanggalMasuk` date NOT NULL,
		  `hargaBeli` double NOT NULL,
		  `hargaJual` double NOT NULL,
		  `kodeGudang` varchar(64) NOT NULL,
		  `pemasok` varchar(64) NOT NULL,
		  `stok` int(11) NOT NULL,
		  `kurs` varchar(10) NOT NULL,
		  `saldoAwal` double NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_data_produk`
		--

		CREATE TABLE IF NOT EXISTS `gd_data_produk` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeBarang` varchar(64) NOT NULL,
		  `deskripsi` text NOT NULL,
		  `kodeSatuan` varchar(20) NOT NULL,
		  `hpp` double NOT NULL,
		  `namaBarang` varchar(100) NOT NULL,
		  `sifat` varchar(10) NOT NULL,
		  `stok` int(11) NOT NULL,
		  `noAkunPenjualan` varchar(10) NOT NULL,
		  PRIMARY KEY (`id`),
		  UNIQUE KEY `kodeBarang` (`kodeBarang`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_detail_bank_keluar`
		--

		CREATE TABLE IF NOT EXISTS `gd_detail_bank_keluar` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `noAkunDetail` varchar(10) NOT NULL,
		  `nilaiDetail` double NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_detail_bank_masuk`
		--

		CREATE TABLE IF NOT EXISTS `gd_detail_bank_masuk` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `noAkunDetail` varchar(10) NOT NULL,
		  `nilaiDetail` double NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_detail_kas_keluar`
		--

		CREATE TABLE IF NOT EXISTS `gd_detail_kas_keluar` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `noAkunDetail` varchar(10) NOT NULL,
		  `nilaiDetail` double NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_detail_kas_masuk`
		--

		CREATE TABLE IF NOT EXISTS `gd_detail_kas_masuk` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `noAkunDetail` varchar(10) NOT NULL,
		  `nilaiDetail` double NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_detail_transaksi_jurnal`
		--

		CREATE TABLE IF NOT EXISTS `gd_detail_transaksi_jurnal` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `noAkunJurnal` varchar(10) NOT NULL,
		  `kodeDepartemen` varchar(64) NOT NULL,
		  `debit` double NOT NULL,
		  `kredit` double NOT NULL,
		  `tanggal` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_fase_proyek`
		--

		CREATE TABLE IF NOT EXISTS `gd_fase_proyek` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeProyek` varchar(64) NOT NULL,
		  `namaFase` varchar(128) NOT NULL,
		  `deskripsiFase` text NOT NULL,
		  `anggaranBiaya` double NOT NULL,
		  `realisasiBiaya` double NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_harta_tetap`
		--

		CREATE TABLE IF NOT EXISTS `gd_harta_tetap` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `namaAset` varchar(128) NOT NULL,
		  `hargaBeli` double NOT NULL,
		  `umurEkonomis` int(11) NOT NULL,
		  `lastActivity` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
		  `noAkunAset` varchar(10) NOT NULL,
		  `noAkunPenyusutan` varchar(10) NOT NULL,
		  `tanggalBeli` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
		  `penyusutanBulan` double NOT NULL,
		  `terhitungTanggal` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
		  `bebanBulan` double NOT NULL,
		  `nilaiBuku` double NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_hutang`
		--

		CREATE TABLE IF NOT EXISTS `gd_hutang` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `noInvoice` varchar(64) NOT NULL,
		  `noReferensi` varchar(64) NOT NULL,
		  `tanggal` date NOT NULL,
		  `kodePelanggan` varchar(64) NOT NULL,
		  `catatan` varchar(512) NOT NULL,
		  `jumlahPenerimaan` double NOT NULL,
		  `jumlahTagihan` double NOT NULL,
		  `noAkunKas` varchar(10) NOT NULL,
		  `noAkunPiutang` varchar(10) NOT NULL,
		  `pembayaranKe` tinyint(4) NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_invoice_penjualan`
		--

		CREATE TABLE IF NOT EXISTS `gd_invoice_penjualan` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeTransaksi` varchar(10) NOT NULL,
		  `noSalesOrder` varchar(64) NOT NULL,
		  `kodePelanggan` varchar(64) NOT NULL,
		  `tanggal` date NOT NULL,
		  `catatan` varchar(512) NOT NULL,
		  `nilai` double NOT NULL,
		  `hargaPokok` double NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_jurnal_memorial`
		--

		CREATE TABLE IF NOT EXISTS `gd_jurnal_memorial` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `noReferensi` varchar(64) NOT NULL,
		  `tanggal` date NOT NULL,
		  `catatan` varchar(512) NOT NULL,
		  `jumlahUang` double NOT NULL,
		  `noAkunPiutang` varchar(10) NOT NULL,
		  `noAkunMemorial` varchar(10) NOT NULL,
		  `tipe` tinyint(4) NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_kas_keluar`
		--

		CREATE TABLE IF NOT EXISTS `gd_kas_keluar` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `tanggal` date NOT NULL,
		  `catatan` varchar(512) NOT NULL,
		  `nilaiTotal` double NOT NULL,
		  `noAkunKas` varchar(10) NOT NULL,
		  `kodePelanggan` varchar(64) NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_kas_masuk`
		--

		CREATE TABLE IF NOT EXISTS `gd_kas_masuk` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `tanggal` date NOT NULL,
		  `catatan` varchar(512) NOT NULL,
		  `nilaiTotal` double NOT NULL,
		  `noAkunKas` varchar(10) NOT NULL,
		  `kodePelanggan` varchar(64) NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_kelompok_barang`
		--

		CREATE TABLE IF NOT EXISTS `gd_kelompok_barang` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeKelompok` varchar(64) NOT NULL,
		  `namaKelompok` varchar(128) NOT NULL,
		  `noAkunHpp` varchar(8) NOT NULL,
		  `noAkunPenjualan` varchar(8) NOT NULL,
		  `noAkunPersediaan` varchar(8) NOT NULL,
		  `noAkunKonsinyasi` varchar(8) NOT NULL,
		  `noAkunReturPenjualan` varchar(8) NOT NULL,
		  `noAkunPengiriman` varchar(8) NOT NULL,
		  PRIMARY KEY (`id`),
		  UNIQUE KEY `kodeKelompok` (`kodeKelompok`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_kelompok_transaksi`
		--

		CREATE TABLE IF NOT EXISTS `gd_kelompok_transaksi` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeKelompok` varchar(2) NOT NULL,
		  `keterangan` varchar(128) NOT NULL,
		  PRIMARY KEY (`id`),
		  UNIQUE KEY `kodeKelompok` (`kodeKelompok`)
		) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=24 ;

		--
		-- Dumping data for table `gd_kelompok_transaksi`
		--

		INSERT INTO `gd_kelompok_transaksi` (`id`, `kodeKelompok`, `keterangan`) VALUES
		(1, 'GJ', 'General Journal'),
		(2, 'CD', 'Cash Deposit'),
		(3, 'CR', 'Cash Receive'),
		(4, 'SJ', 'Sales'),
		(5, 'PJ', 'Purchase'),
		(6, 'IJ', 'Inventory'),
		(7, 'SD', 'Sales Discount'),
		(9, 'SF', 'Late Charges (Sales)'),
		(10, 'PF', 'Late Charges (Buy)'),
		(11, 'MR', 'Material Requisition'),
		(12, 'SQ', 'Sales Quotation'),
		(13, 'RQ', 'Request for Quotation'),
		(14, 'PO', 'Purchase Order'),
		(15, 'SO', 'Sales Order'),
		(16, 'CI', 'Consignment In'),
		(17, 'CO', 'Consignment Return'),
		(18, 'PR', 'Purchase Return'),
		(19, 'SR', 'Sales Return'),
		(20, 'DO', 'Sales Delivery Order'),
		(21, 'PD', 'Purchase Delivery Order'),
		(22, 'PA', 'Purchase Advance'),
		(23, 'SA', 'Sales Advance');

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_klasifikasi`
		--

		CREATE TABLE IF NOT EXISTS `gd_klasifikasi` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `noKlasifikasi` tinyint(4) NOT NULL,
		  `namaKlasifikasi` varchar(100) NOT NULL,
		  `namaAliasKlasifikasi` varchar(100) NOT NULL,
		  PRIMARY KEY (`id`),
		  UNIQUE KEY `noKlasifikasi` (`noKlasifikasi`)
		) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

		--
		-- Dumping data for table `gd_klasifikasi`
		--

		INSERT INTO `gd_klasifikasi` (`id`, `noKlasifikasi`, `namaKlasifikasi`, `namaAliasKlasifikasi`) VALUES
		(1, 1, 'Aktiva', 'Aset'),
		(2, 2, 'Pasiva', 'Kewjiban/Liability'),
		(3, 3, 'Ekuitas', 'Modal'),
		(4, 4, 'Pendapatan', 'Hasil Penjualan'),
		(5, 5, 'Biaya Operasional', 'Beban Operasional'),
		(6, 6, 'Biaya Non-operasional', 'Beban Non-operasional'),
		(7, 7, 'Pendapatan & Biaya Lain-Lain', 'Lain-lain');

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_mata_uang`
		--

		CREATE TABLE IF NOT EXISTS `gd_mata_uang` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeMatauang` varchar(64) NOT NULL,
		  `namaMatauang` varchar(64) NOT NULL,
		  `simbol` varchar(5) NOT NULL,
		  `kursTukar` double NOT NULL DEFAULT '1',
		  `isDefault` tinyint(1) NOT NULL DEFAULT '0',
		  PRIMARY KEY (`id`),
		  UNIQUE KEY `kodeMatauang` (`kodeMatauang`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_nama_alamat`
		--

		CREATE TABLE IF NOT EXISTS `gd_nama_alamat` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodePelanggan` varchar(64) NOT NULL,
		  `namaPelanggan` varchar(256) NOT NULL,
		  `tipe` varchar(32) NOT NULL,
		  `npwp` varchar(64) NOT NULL,
		  `diskon` double NOT NULL,
		  `jatuhtempo` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
		  `diskonAwal` double NOT NULL,
		  `dendaKeterlambatan` int(11) NOT NULL,
		  `alamat` varchar(512) NOT NULL,
		  `kontak` varchar(64) NOT NULL,
		  `noAkunPiutang` varchar(10) NOT NULL,
		  `noAkunHutang` double NOT NULL,
		  `saldo` double NOT NULL,
		  PRIMARY KEY (`id`),
		  UNIQUE KEY `kodePelanggan` (`kodePelanggan`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_order_pembelian`
		--

		CREATE TABLE IF NOT EXISTS `gd_order_pembelian` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `noAkunPembelian` varchar(10) NOT NULL,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `kodePelanggan` varchar(64) NOT NULL,
		  `kodeBarang` varchar(64) NOT NULL,
		  `jumlah` int(11) NOT NULL,
		  `harga` double NOT NULL,
		  `diskom` double NOT NULL,
		  `kodePajak` varchar(64) NOT NULL,
		  `retur` int(11) NOT NULL,
		  `isDibayar` tinyint(1) NOT NULL DEFAULT '0',
		  `isDikirim` tinyint(1) NOT NULL DEFAULT '0',
		  `kodeMatauang` varchar(64) NOT NULL,
		  `JumlahDibayar` double NOT NULL,
		  `kodeTOS` varchar(64) NOT NULL,
		  `kodeTOP` varchar(64) NOT NULL,
		  `biayaKirim` double NOT NULL,
		  `alamatKirim` varchar(512) NOT NULL,
		  PRIMARY KEY (`id`),
		  UNIQUE KEY `kodeTransaksi` (`kodeTransaksi`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_order_penjualan`
		--

		CREATE TABLE IF NOT EXISTS `gd_order_penjualan` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `kodePelanggan` varchar(64) NOT NULL,
		  `tanggal` date NOT NULL,
		  `kodeBarang` varchar(64) NOT NULL,
		  `kodeSatuan` varchar(64) NOT NULL,
		  `jumlah` double NOT NULL,
		  `hargaJual` double NOT NULL,
		  `hpp` double NOT NULL,
		  `disc` double NOT NULL,
		  `total` double NOT NULL,
		  `pajak` double NOT NULL,
		  `totalPajak` double NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_pembelian_barang`
		--

		CREATE TABLE IF NOT EXISTS `gd_pembelian_barang` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `noInvoice` varchar(64) DEFAULT NULL,
		  `noPO` varchar(64) DEFAULT NULL,
		  `namaBarang` varchar(128) NOT NULL,
		  `kodeVendor` varchar(64) NOT NULL,
		  `hargaBarang` double NOT NULL,
		  `jumlahBarang` double NOT NULL,
		  `satuan` varchar(64) NOT NULL,
		  `totalHarga` double NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_periode_akuntansi`
		--

		CREATE TABLE IF NOT EXISTS `gd_periode_akuntansi` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodePerusahaan` varchar(64) NOT NULL,
		  `bulan` tinyint(4) NOT NULL,
		  `tahun` smallint(6) NOT NULL,
		  `bulanTutupBuku` tinyint(4) NOT NULL,
		  `kodeDepartemen` varchar(64) NOT NULL,
		  `namaDepartemen` varchar(64) NOT NULL,
		  `prefix` varchar(16) NOT NULL,
		  `format` varchar(32) NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_piutang`
		--

		CREATE TABLE IF NOT EXISTS `gd_piutang` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `noInvoice` varchar(64) NOT NULL,
		  `noReferensi` varchar(64) NOT NULL,
		  `tanggal` date NOT NULL,
		  `kodePelanggan` varchar(64) NOT NULL,
		  `catatan` varchar(512) NOT NULL,
		  `jumlahPenerimaan` double NOT NULL,
		  `jumlahTagihan` double NOT NULL,
		  `noAkunKas` varchar(10) NOT NULL,
		  `noAkunPiutang` varchar(10) NOT NULL,
		  `pembayaranKe` tinyint(4) NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_proyek`
		--

		CREATE TABLE IF NOT EXISTS `gd_proyek` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeProyek` varchar(64) NOT NULL,
		  `namaProyek` varchar(128) NOT NULL,
		  `kodePenjab` varchar(64) NOT NULL,
		  `progress` double NOT NULL,
		  `tanggalMulai` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
		  `tanggalSelesai` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
		  `anggaranTotal` double NOT NULL,
		  `realisasiTotal` double NOT NULL,
		  `isFase` tinyint(1) NOT NULL,
		  PRIMARY KEY (`id`),
		  UNIQUE KEY `kodeProyek` (`kodeProyek`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_rekening_jurnal`
		--

		CREATE TABLE IF NOT EXISTS `gd_rekening_jurnal` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `noAkun` varchar(8) NOT NULL,
		  `namaAkun` varchar(200) NOT NULL,
		  `namaAliasAkun` varchar(200) NOT NULL,
		  `saldoAwal` double NOT NULL,
		  `saldoSekarang` double NOT NULL,
		  `isKas` tinyint(2) NOT NULL,
		  PRIMARY KEY (`id`),
		  UNIQUE KEY `noAkun` (`noAkun`)
		) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=90 ;

		--
		-- Dumping data for table `gd_rekening_jurnal`
		--

		INSERT INTO `gd_rekening_jurnal` (`id`, `noAkun`, `namaAkun`, `namaAliasAkun`, `saldoAwal`, `saldoSekarang`, `isKas`) VALUES
		(1, '11000010', 'Kas Kecil', '', 0, 0, 1),
		(2, '11000020', 'Kas', '', 0, 0, 1),
		(3, '12000010', 'Bank (IDR)', '', 0, 0, 2),
		(4, '12000020', 'Bank (USD)', '', 0, 0, 2),
		(5, '13000010', 'Piutang Giro', '', 0, 0, 0),
		(6, '13000020', 'Piutang Usaha (IDR)', '', 0, 0, 0),
		(7, '13000030', 'Piutang Usaha (USD)', '', 0, 0, 0),
		(8, '13000040', 'Cadangan Kerugian Piutang', '', 0, 0, 0),
		(9, '14000010', 'Persediaan 1', '', 0, 0, 0),
		(10, '14000020', 'Persediaan 2', '', 0, 0, 0),
		(11, '14000030', 'Persediaan 3', '', 0, 0, 0),
		(12, '14000040', 'Persediaan 4', '', 0, 0, 0),
		(13, '15000010', 'Pajak Dibayar di Muka', '', 0, 0, 0),
		(14, '15000020', 'Asuransi Dibayar di Muka', '', 0, 0, 0),
		(15, '16000010', 'Investasi Saham', '', 0, 0, 0),
		(16, '16000020', 'Investasi Obligasi', '', 0, 0, 0),
		(17, '17000010', 'Tanah', '', 0, 0, 0),
		(18, '17000020', 'Bangunan', 'Property', 0, 0, 0),
		(19, '17600021', 'Akumulasi Penyusutan Bangunan', '', 0, 0, 0),
		(20, '17000030', 'Masin dan Peralatan', '', 0, 0, 0),
		(21, '17600031', 'Akumulasi Penyusutan Mesin dan Peralatan', '', 0, 0, 0),
		(22, '17000040', 'Mebel dan Alat Tulis Kantor', '', 0, 0, 0),
		(23, '17600041', 'Akumulasi Penyusutan Mebel & ATK', '', 0, 0, 0),
		(24, '17000050', 'Kendaraan', '', 0, 0, 0),
		(25, '17600051', 'Akumulasi Penyusutan Kendaraan', '', 0, 0, 0),
		(26, '17000070', 'Harta Lainnya', '', 0, 0, 0),
		(27, '17600071', 'Akumulasi Penyusutan Harta Lainnya', '', 0, 0, 0),
		(28, '18000010', 'Hak Merek', '', 0, 0, 0),
		(29, '18000020', 'Hak Cipta', '', 0, 0, 0),
		(30, '18000030', 'Good Will', '', 0, 0, 0),
		(31, '21000010', 'Wesel Bayar', '', 0, 0, 0),
		(32, '21000015', 'Hutang Giro', '', 0, 0, 0),
		(33, '21000020', 'Hutang Usaha (IDR)', '', 0, 0, 0),
		(34, '21000025', 'Hutang Usaha (USD)', '', 0, 0, 0),
		(35, '21000030', 'Hutang Konsinyasi', '', 0, 0, 0),
		(36, '21000040', 'Uang Muka Penjualan', '', 0, 0, 0),
		(37, '21000055', 'Hutang Deviden', '', 0, 0, 0),
		(38, '21000060', 'Hutang Bunga', '', 0, 0, 0),
		(39, '21000075', 'Kartu Kredit', '', 0, 0, 0),
		(40, '21000080', 'Hutang Pajak Pennjualan', '', 0, 0, 0),
		(41, '21000085', 'Hutang Gaji', '', 0, 0, 0),
		(42, '22000010', 'Sewa Diterima di Muka', '', 0, 0, 0),
		(43, '23000010', 'Pinjaman Hipotik', '', 0, 0, 0),
		(44, '23000020', 'Hutang Bank', '', 0, 0, 0),
		(45, '31000010', 'Saham Preferen', '', 0, 0, 0),
		(46, '31000020', 'Modal Disetor', '', 0, 0, 0),
		(47, '31000030', 'Saham Biasa', '', 0, 0, 0),
		(48, '32000010', 'Laba Ditahan', '', 0, 0, 0),
		(49, '32000020', 'Laba Tahun Berjalan', '', 0, 0, 0),
		(50, '32000099', 'Historical Balancing', '', 0, 0, 0),
		(51, '41000001', 'Penjualan Barang Scam', '', 0, 0, 0),
		(52, '41000002', 'Penjualan obongkar', '', 0, 0, 0),
		(53, '41000003', 'Penjualan meneh', '', 0, 0, 0),
		(54, '41000004', 'Penjualan bbm', '', 0, 0, 0),
		(55, '41000070', 'Potongan Penjualan', '', 0, 0, 0),
		(56, '41000080', 'Pendapatan Denda Keterlambatan', '', 0, 0, 0),
		(57, '41000090', 'Pendapatan atas Pengiriman', '', 0, 0, 0),
		(58, '51000010', 'HPP Produk 1', '', 0, 0, 0),
		(59, '51000020', 'HPP Produk 2', '', 0, 0, 0),
		(60, '51000030', 'HPP Produk 3', '', 0, 0, 0),
		(61, '51000070', 'Potongan Pembelian', '', 0, 0, 0),
		(62, '51000080', 'Biaya atas Pengiriman barang', '', 0, 0, 0),
		(63, '52000010', 'Kerugian Piutang', '', 0, 0, 0),
		(64, '52000020', 'Biaya Denda Keterlambatan', '', 0, 0, 0),
		(65, '52000030', 'Kerusakan dan Kegagalan Material', '', 0, 0, 0),
		(66, '61000010', 'Gaji Direksi dan Karyawan', '', 0, 0, 0),
		(67, '62000010', 'Biaya Listrik,Air,& Telpon', '', 0, 0, 0),
		(68, '62000020', 'Administrasi Kantor', '', 0, 0, 0),
		(69, '62000030', 'Promosi dan Iklan', '', 0, 0, 0),
		(70, '65000010', 'Parkir & BBM Kendaraan', '', 0, 0, 0),
		(71, '66000010', 'Penyusutan Bangunan', '', 0, 0, 0),
		(72, '66000011', 'Penyusutan Mesin dan Peralatan', '', 0, 0, 0),
		(73, '66000012', 'Penyusutan  Mebel dan ATK', '', 0, 0, 0),
		(74, '66000013', 'Penyusutan Kendaraan', '', 0, 0, 0),
		(75, '66000015', 'Penyusutan Harta Lainnya', '', 0, 0, 0),
		(76, '66000017', 'Amortisasi Pra Operasi dan Operasi', '', 0, 0, 0),
		(77, '71000010', 'Laba Rugi Selisih Kurs', '', 0, 0, 0),
		(78, '71000020', 'Hasil Sewa Tanah', '', 0, 0, 0),
		(79, '76000010', 'Biaya Bunga', '', 0, 0, 0),
		(80, '76000020', 'Jasa Bank', '', 0, 0, 0),
		(81, '51000040', 'Komisi Penjualan', '', 0, 0, 0),
		(82, '21000082', 'Hutang Komisi Penjualan', '', 0, 0, 0),
		(87, '13000003', 'Piutang Panjul Akhzan', '', 0, 0, 0),
		(88, '41000006', 'Penjualan Jasa Pengecatan', 'ya ngecet umah', 0, 0, 0),
		(89, '71000030', 'Kelebihan Pembayaran Piutang', '', 0, 0, 0);

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_satuan_pengukuran`
		--

		CREATE TABLE IF NOT EXISTS `gd_satuan_pengukuran` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeSatuan` varchar(64) NOT NULL,
		  `namaSatuan` varchar(64) NOT NULL,
		  `keterangan` varchar(128) NOT NULL,
		  `faktorPengali` double NOT NULL DEFAULT '0',
		  `kodeSatuanParent` varchar(64) DEFAULT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_tabel_info_perusahaan`
		--

		CREATE TABLE IF NOT EXISTS `gd_tabel_info_perusahaan` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodePerusahaan` varchar(64) NOT NULL,
		  `namaPerusahaan` varchar(100) NOT NULL,
		  `alamat` varchar(512) NOT NULL,
		  `kota` varchar(64) NOT NULL,
		  `negara` varchar(64) NOT NULL,
		  `kodePos` varchar(16) NOT NULL,
		  `telp` varchar(16) NOT NULL,
		  `email` varchar(32) NOT NULL,
		  `web` varchar(32) NOT NULL,
		  `jenisUsaha` varchar(32) NOT NULL,
		  `kodeMatauang` int(11) NOT NULL,
		  PRIMARY KEY (`id`),
		  UNIQUE KEY `kodePerusahaan` (`kodePerusahaan`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_top`
		--

		CREATE TABLE IF NOT EXISTS `gd_top` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeTOP` varchar(64) NOT NULL,
		  `namaTOP` varchar(64) NOT NULL,
		  `isiTOP` text NOT NULL,
		  `keterangan` varchar(512) NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_tos`
		--

		CREATE TABLE IF NOT EXISTS `gd_tos` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeTOS` varchar(64) NOT NULL,
		  `namaTOS` varchar(64) NOT NULL,
		  `isiTOS` text NOT NULL,
		  `keterangan` varchar(512) NOT NULL,
		  PRIMARY KEY (`id`),
		  UNIQUE KEY `kodeTOS` (`kodeTOS`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_transaksi_jurnal`
		--

		CREATE TABLE IF NOT EXISTS `gd_transaksi_jurnal` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `catatan` varchar(256) NOT NULL,
		  `nilaiTransaksi` double NOT NULL,
		  `tanggal` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
		  PRIMARY KEY (`id`),
		  UNIQUE KEY `kodeTransaksi` (`kodeTransaksi`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_uang_muka`
		--

		CREATE TABLE IF NOT EXISTS `gd_uang_muka` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `noReferensi` varchar(64) NOT NULL,
		  `tanggal` date NOT NULL,
		  `catatan` varchar(512) NOT NULL,
		  `jumlahUang` double NOT NULL,
		  `kodePelanggan` varchar(64) NOT NULL,
		  `noAkunKas` varchar(10) NOT NULL,
		  `noAkunUangMuka` int(11) NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_user`
		--

		CREATE TABLE IF NOT EXISTS `gd_user` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `username` varchar(64) NOT NULL,
		  `password` varchar(64) NOT NULL,
		  `level` tinyint(4) NOT NULL,
		  `lastActivity` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
		  PRIMARY KEY (`id`),
		  UNIQUE KEY `username` (`username`)
		) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

		/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
		/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
		/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
		"""

		
		pass
	
	def Execute(self):
		#~ f = open("creator.md","w")
		#~ f.write(self.sqldump)
		#~ f.close()
		#~ f = open("creator.md","r")
		#~ subprocess.check_call(self.si_om.BasePath[:-1]+"\\mysql\\bin\\mysql.exe --port=44559 -u root test",stdin=f,shell=True)
		#~ f.close()
		#~ subprocess.check_call(self.si_om.BasePath+"mysql/bin/echo.exe < "+"creator.md")
		#~ self.si_om.DatabaseRunQuery(self.sqldump)
		#---- ga bisa pakai runQuery --- commit harus menunggu beberapa detik
		#---- new attempt: exclusive mysqldb
		try:
			self.db = MySQLdb.connect(self.si_om.dbHost,self.si_om.dbUser,self.si_om.dbPass,self.si_om.dbDatabase)
			print ("connected database to generic mysql port")
		except:
			try:
				print "gagal"
				self.db = MySQLdb.Connect(host=self.si_om.dbHost, port=self.si_om.dbPort, user=self.si_om.dbUser, passwd=self.si_om.dbPass, db=self.si_om.dbDatabase)
				print ("connected database to Garvin port")
			except:
				print "gagal"
				#~ exit (1)
		#-- sudah terkoneksi, bentuk cursor
		try:
			self.cursor = self.db.cursor()
		except:return
		self.cursor.execute(self.sqldump)
		self.creatortimer = QtCore.QTimer(self.si_om)
		self.creatortimer.timeout.connect(self.Selesai)
		self.creatortimer.start(4000)
		
	def Selesai(self):
		self.db.commit()
		self.creatortimer.stop()
		print "commited"
		self.db.close()
		
	def close(self):
		self.sqldump=None
		self.si_om=None
		#--- let the garbage collector work

